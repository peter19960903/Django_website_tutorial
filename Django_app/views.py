from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import account_info
from django.urls import reverse, reverse_lazy
from django.contrib import auth
from django.shortcuts import render


class OrderCreateView(CreateView):
    # template_name = "Django_app/account_info.html"
    model = account_info
    fields = "__all__"
    success_url = reverse_lazy("Order_System:finish")
    

class FinishView(TemplateView):
    template_name = "Django_app/finish.html"


class OrderListView(ListView):
    # model_list.html
    model = account_info
    #context_object_name = Order_list
    # queryset = account_info.objects.all()

class OrderDetailView(DetailView):
    #account_info_detail.html
    # context_object_name = 'ouo'
    model = account_info

class OrderUpdateView(UpdateView):
    model = account_info
    fields = ['account_email', 'account_order']
    template_name = 'Django_app/account_info_update.html'
    success_url = reverse_lazy("Order_System:finish")


class OrderDeleteView(DeleteView):
    model = account_info
    success_url = reverse_lazy("Order_System:Odrer")