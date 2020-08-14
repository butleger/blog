import datetime
from .db_getters import *
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .forms import AddArticleForm, AddCommentForm
from django.utils.decorators import classonlymethod
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse, HttpResponseRedirect
from .base import BaseBlogView, BaseAjaxWorker


class ArticlesView(BaseBlogView):
    template_name = 'navigate_menu\\articles.html'

    extra_context = {
        'articles': getAllArticles(),
    }


class AboutMeView(BaseBlogView):
    template_name = 'navigate_menu\\about_me.html'

    extra_context = {
        'text': getSingleArticleByName('About me').text
    }


class ContactsView(BaseBlogView):
    template_name = 'navigate_menu\\contacts.html'

    extra_context = {
        'text': getSingleArticleByName('Contacts').text
    }


class MyResourcesView(BaseBlogView):
    template_name = 'navigate_menu\\my_resources.html'

    extra_context = {
        'text': getSingleArticleByName('My resources').text
    }


class MyWorksView(BaseBlogView):
    template_name = 'navigate_menu\\my_works.html'

    extra_context = {
        'text': getSingleArticleByName('My works').text
    }


class ArticleView(BaseBlogView):
    #article and comments will cant be getted,cause depends from view arguments
    #so it will be define in next functions
    comments = None
    article = None
    comment_form = AddCommentForm
    template_name = 'article.html'

    extra_context = {
        'comment_form': comment_form(),
    }

    def post(self, request, *args, **kwargs):
        print('args = ', *args)
        print('kwargs = ', kwargs)
        commentForm = AddCommentForm(request.POST)
        if commentForm.is_valid():
            try:
                article = getArticleById(kwargs['articleId'])
            except :
                return HttpResponseRedirect('/articles/' + str(kwargs['articleId']))
            comment = CommentModel()
            comment.article = article
            comment.author = request.POST.get('author')
            comment.text = request.POST.get('text')
            comment.date = datetime.datetime.now()
            comment.save()
        else:
            render(request, "all_fucked.html")
        return HttpResponseRedirect('/articles/' + str(kwargs['articleId']))

    #added more context that depends from url in setup
    def get_context_data(self, **kwargs):
        self.extra_context.update(article=self.article)
        self.extra_context.update(comments=getCommentsByArticle(self.article))
        return super().get_context_data(**kwargs)

    def setup(self, request, *args, **kwargs):
        self.article = getArticleById(int(kwargs['articleId']))
        return super().setup(request, *args, **kwargs)


class LikeAdder(BaseAjaxWorker):
    request_arg_names = ['id']

    def request_callback(self):
        try:
            comment = getCommentById(self.request_data['id'])
        except:
            self.status = 404
        else:
            comment.likes += 1
            comment.save()


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
        else:
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
    print(request.session.items())
    return redirect('articles:base_page')


def shouldBeLogged(request):
    return render(request, 'should_logging.html')

