from django.urls import path, re_path
from . import views
from django.urls import include


app_name = 'articles'
urlpatterns = [
    path('', views.ArticlesView.as_view(), name='base_page'),
    path('test', views.BaseAjaxWorker.as_view(), name='test'),
    path('<id>/likes', views.addLike, name='service_add_like'),
    path('about_me', views.AboutMeView.as_view(), name='about_me'),
    path('my_works', views.MyWorksView.as_view(), name='my_works'),
    path('my_resources', views.MyResourcesView.as_view(), name='my_resources'),
    path('contacts', views.ContactsView.as_view(), name='contacts'),
    path('articles', views.badRedirect, name='bad_redirect'),
    path('not_logged', views.shouldBeLogged, name='not_logged'),
    path('<int:articleId>', views.ArticleView.as_view(), name='solo_article'),
]