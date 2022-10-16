from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import account_info
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.contrib.auth.models import User



class OrderCreateView(LoginRequiredMixin, CreateView):
    # template_name = "Django_app/account_info.html"
    login_url = "/login"
    model = account_info
    fields = ["account_name","account_email", "account_order"]
    success_url = reverse_lazy("Order_System:finish")
   
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

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