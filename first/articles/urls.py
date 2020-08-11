from django.urls import path, re_path
from . import views
from django.urls import include


app_name = 'articles'
urlpatterns = [
    path('', views.articles, name='base_page'),
    path('<id>/likes', views.addLike, name='service_add_like'),
    path('about_me', views.about_me, name='about_me'),
    path('my_works', views.my_works, name='my_works'),
    path('my_resources', views.my_resources, name='my_resources'),
    path('contacts', views.contacts, name='contacts'),
    path('articles', views.badRedirect, name='bad_redirect'),
    path('sign_in',views.registrate, name='register_user' ),
    path('not_logged', views.shouldBeLogged, name='not_logged'),
    path('<articleId>', views.sendArticle, name='solo_article'),
]