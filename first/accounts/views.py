from django.shortcuts import render
from articles.db_getters import *
from articles.exceptions import *
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import TemplateView
from django.urls import reverse


class MyLoginView(LoginView):
    redirect_authenticated_user_template = 'accounts:success_login'
    template_name = 'registration\\login.html'
    extra_context = {
        'menu': getMenu(),
        'footer': getFooter()
    }

    def get_redirect_url(self):
        return reverse(self.redirect_authenticated_user)

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

# Create your views here.
