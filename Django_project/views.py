from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, CreateView
from django.urls import reverse, reverse_lazy
from django.contrib import auth
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

MAIN_PAGE_URL = '/main_page'

def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(MAIN_PAGE_URL)
    
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    user = auth.authenticate(username=username, password=password)
    
    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect(MAIN_PAGE_URL)
    else:
        return render(request, 'login.html', locals())

def main_page(request):
    return render(request, 'main_page.html')

def log_out(request):
    auth.logout(request)
    return HttpResponseRedirect(MAIN_PAGE_URL)



class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'sign_up.html'

