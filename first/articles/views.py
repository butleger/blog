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
    footer = getFooter()
    menu = getMenu()
    outArticles = getAllArticles()
    return render(request, 'navigate_menu\\articles.html', {'articles': outArticles, 'menu': menu, 'footer': footer})


def addLike(request, id):
    if request.method == 'GET':
        try:
            comment = getCommentById(commentId=request.GET.get('id'))
        except CustomException as ex:
            return HttpResponse(status=404)#render(request, 'all_fucked', getAllFuckedContent(ex), status=404)
        else:
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
            pass
        else :
            comment.article = _article
            comment.save()
    menu = getMenu()
    footer = getFooter()
    article = getArticleById(articleId)
    comments = getCommentsByArticle(article)
    return render(request, 'article.html', {'article': article,
                                            'comments': comments,
                                            'menu': menu,
                                            'comment_form': AddCommentForm(),
                                            'footer': footer})


@login_required
def about_me(request):
    menu = getMenu()
    footer = getFooter()
    return render(request, 'navigate_menu\\about_me.html', {'menu': menu, 'footer': footer})


def contacts(request):
    menu = getMenu()
    footer = getFooter()
    return render(request, 'navigate_menu\\contacts.html', {'menu': menu, 'footer':footer})


def my_resources(request):
    menu = getMenu()
    footer = getFooter()
    return render(request, 'navigate_menu\\my_resources.html', {'menu': menu, 'footer': footer})

def my_works(request):
    menu = getMenu()
    footer = getFooter()
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


def badRedirect(request):
    return redirect('article')


def shouldBeLogged(request):
    return render(request, 'should_logging.html')



# Create your views here.
