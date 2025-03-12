from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import FormView
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from expenses.models import Category



class CategoryCreate(LoginRequiredMixin,CreateView):
    model=Category
    fields=['name']
    login_url='login'
    success_url="view_category"
    def form_valid(self, form):
        form.instance.owner=self.request.user
        return super().form_valid(form)
    
class CategoryRetrieve(LoginRequiredMixin,ListView):
    model=Category
    fields=['name']    
    success_url="view_category"
    login_url='login'
    def get_queryset(self):
        return Category.objects.filter(owner=self.request.user)
        
class CategoryUpdate(LoginRequiredMixin,UpdateView):
    model=Category
    fields=['name']
    success_url="view_category"
    login_url='login'
    def get_queryset(self):
        #filtering query set

        return Category.objects.filter(owner=self.request.user)
      
class CategoryDelete(LoginRequiredMixin,DeleteView):
    model=Category
    fields=['name']
    success_url=reverse_lazy('view_category') 
    login_url='login'
    def get_queryset(self):
        #filtering query set

        return Category.objects.filter(owner=self.request.user)
    

    
    


    