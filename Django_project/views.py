from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, CreateView
from django.urls import reverse, reverse_lazy
from django.contrib import auth
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

class home_view(TemplateView):
    template_name = 'home.html'

def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/main_page')
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('/main_page')
    else:
        return render(request, 'login.html', locals())

def main_page(request):
    return render(request, 'main_page.html')

def log_out(request):
    auth.logout(request)
    return HttpResponseRedirect('/main_page')



class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'sign_up.html'

