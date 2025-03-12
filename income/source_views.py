from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import FormView
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from income.models import Source



class SourceCreate(LoginRequiredMixin,CreateView):
    model=Source
    fields=['name']
    login_url='login'
    success_url="show_income"
    def form_valid(self, form):
        form.instance.owner=self.request.user
        return super().form_valid(form)
    
class SourceRetrieve(LoginRequiredMixin,ListView):
    model=Source
    fields=['name']    
    success_url="show_income"
    login_url='login'
    def get_queryset(self):
        return Source.objects.filter(owner=self.request.user)
        
class SourceUpdate(LoginRequiredMixin,UpdateView):
    model=Source
    fields=['name']
    success_url="show_income"
    login_url='login'
    def get_queryset(self):
        #filtering query set

        return Source.objects.filter(owner=self.request.user)
      
class SourceDelete(LoginRequiredMixin,DeleteView):
    model=Source
    fields=['name']
    success_url=reverse_lazy('show_income') 
    login_url='login'
    def get_queryset(self):
        #filtering query set

        return Source.objects.filter(owner=self.request.user)
    

    
    


    