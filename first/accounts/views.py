from django.shortcuts import render
from articles.db_getters import *
from articles.exceptions import *
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import TemplateView
from django.urls import reverse
from .forms import AuthWithRememberingSession


class MyLoginView(LoginView):
    #form should have field 'remember_me'
    #if form have not remove post function in this class
    form_class = AuthWithRememberingSession
    success_redirect_template = 'accounts:success_login'
    template_name = 'registration\\login.html'
    extra_context = {
        'menu': getMenu(),
        'footer': getFooter()
    }

    def get_redirect_url(self):
        return reverse(self.success_redirect_template)

    def post(self, request, *args, **kwargs):
        print('this is post function in LOGINVIEW and request.POST = ' + str(request.POST))
        if request.POST.get('remember_me', 'No') == 'No':
            #if user dont ask to remember him
            request.session.set_expiry(0)#close session when browser will be ended
        return super().post(request,*args, **kwargs)




class MySuccessLoginView(TemplateView):
    template_name = 'registration\\success_login.html'
    extra_context = {
        'menu': getMenu(),
        'footer': getFooter()
    }


class MyLogoutView(LogoutView):
    extra_context = {
        'menu': getMenu(),
        'footer': getFooter()
    }
    next_page = 'articles:base_page'


def registrate(request):
    menu = getMenu()
    footer = getFooter()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'registration\\registration_complete.html', {'menu': menu,
                                                                                'footer': footer})
        else:
            return render(request, 'registration\\registration_form.html', {'create_user_form': form,
                                                                            'menu': menu,
                                                                            'footer': footer})
    else:
        userCreationForm = UserCreationForm()
        return render(request, 'registration\\registration_form.html', {'create_user_form': userCreationForm,
                                                                        'menu': menu,
                                                                        'footer': footer})

def log_in(request):
    menu = getMenu()
    footer = getFooter()
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'registration\\success_login.html', {'menu': menu,
                                                                        'footer': footer})
        else:
            error = 'There is no user with such password and name'
            return render(request, 'registration\\login.html', {'menu': menu,
                                                                'footer': footer,
                                                                'form': form,
                                                                'errors': error})
    else:
        form = AuthenticationForm()
        return render(request, 'registration\\login.html', {'menu': menu,
                                                            'footer': footer,
                                                            'form': form})
# Create your views here.
