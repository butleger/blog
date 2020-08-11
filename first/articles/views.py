from django.shortcuts import render, redirect
from django.http import (HttpResponse,
                         HttpResponseNotFound,
                         HttpResponsePermanentRedirect,
                         HttpResponseRedirect)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, UserModel
from .forms import AddArticleForm, AddCommentForm
from .models import ArticleModel, CommentModel, MainMenuElementModel
from .exceptions import *
from .db_getters import *
import datetime

def articles(request):
    try:
        footer = getFooter()
        menu = getMenu()
        outArticles = getAllArticles()
    except CustomException as ex:
        return render(request, 'all_fucked.html', getAllFuckedContent(ex))
    return render(request, 'navigate_menu\\articles.html', {'articles': outArticles, 'menu': menu, 'footer': footer})

def addLike(request, id):
    if request.method == 'GET':
        comment = CommentModel()
        try:
            comment = getCommentById(commentId=request.GET.get('id'))
        except CustomException as ex:
            return render(request, 'all_fucked.html',
                          getAllFuckedContent(ex),
                          status=404)
        comment.likes += 1
        comment.save()
        return HttpResponse(status=200)


def sendArticle(request, articleId):
    if request.method == 'POST':
        comment = CommentModel()
        comment.author = request.POST.get('author')
        comment.text = request.POST.get('text')
        comment.date = datetime.datetime.now()
        comment.likes = 0
        try:
            _article = getArticleById(articleId)
        except CustomException as ex:
            return render(request, 'all_fucked.html', getAllFuckedContent(ex), status=404)
        else:
            comment.article = _article
            comment.save()
    try:
        menu = getMenu()
        footer = getFooter()
        article = getArticleById(articleId)
        comments = getCommentsByArticle(article)
    except CustomException as ex:
        return render(request, 'all_fucked.html', getAllFuckedContent(ex), status=404)
    return render(request, 'article.html', {'article': article,
                                            'comments': comments,
                                            'menu': menu,
                                            'comment_form': AddCommentForm(),
                                            'footer': footer})
@login_required
def about_me(request):
    try:
        menu = getMenu()
        footer = getFooter()
    except CustomException as ex:
        return render(request, 'all_fucked.html', getAllFuckedContent(ex))
    return render(request, 'navigate_menu\\about_me.html', {'menu': menu, 'footer': footer})

def contacts(request):
    try:
        menu = getMenu()
        footer = getFooter()
    except CustomException as ex:
        return render(request, 'all_fucked.html', getAllFuckedContent(ex))
    return render(request, 'navigate_menu\\contacts.html', {'menu': menu, 'footer':footer})

def my_resources(request):
    try:
        menu = getMenu()
        footer = getFooter()
    except CustomException as ex:
        return render(request, 'all_fucked.html', getAllFuckedContent(ex))
    return render(request, 'navigate_menu\\my_resources.html', {'menu': menu, 'footer': footer})

def my_works(request):
    try:
        menu = getMenu()
        footer = getFooter()
    except CustomException as ex:
        return render(request, 'all_fucked.html', getAllFuckedContent(ex))
    return render(request, 'navigate_menu\\my_works.html', {'menu': menu,
                                                            'footer': footer,})

def add_comment(request, id):
    if request.method == 'POST':
        commentForm = AddCommentForm(request.POST)
        if commentForm.is_valid():
            try:
                article = getArticleById(id)
            except :
                return HttpResponseRedirect('/articles/' + id)
            comment = CommentModel()
            comment.article = article
            comment.author = request.POST.get('author')
            comment.text = request.POST.get('text')
            comment.date = datetime.datetime.now()
            comment.save()
        else:
            render(request, "all_fucked.html")
    return HttpResponseRedirect('/articles/' + id)

def registrate(request):
    if request.method == 'POST':
        form = UserCreationForm()
        if form.is_valid():
            form.save()
            return render(request, 'registration\\registration_complete.html')
        else:
            return render(request, 'registration\\registration_failed.html')
    else:
        userCreationForm = UserCreationForm()
        return render(request, 'registration\\registration_form.html', {'create_user_form': userCreationForm})

def badRedirect(request):
    return redirect('article')

def shouldBeLogged(request):
    return render(request, 'should_logging.html')



# Create your views here.
