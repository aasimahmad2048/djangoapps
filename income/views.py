from django.shortcuts import render, redirect
from .models import Source, UserIncome
from django.core.paginator import Paginator
from userpreferences.models import UserPreference
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import json

from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse

# Create your views here.
# Create your views here.




@login_required(login_url='/authentication/login')
def search_income(request):
    if request.method == 'POST':
        search_str = json.loads(request.body).get('searchText')
        income = UserIncome.objects.filter(
            amount__istartswith=search_str, owner=request.user) | UserIncome.objects.filter(
            date__istartswith=search_str, owner=request.user) | UserIncome.objects.filter(
            description__icontains=search_str, owner=request.user) | UserIncome.objects.filter(
            source__icontains=search_str, owner=request.user)
        data = income.values()
        return JsonResponse(list(data), safe=False)






@login_required(login_url='/authentication/login')
def index(request):
    categories = Source.objects.all()
    income = UserIncome.objects.filter(owner=request.user)
    paginator = Paginator(income, 5)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)
    currency = UserPreference.objects.get(user=request.user).currency
    context = {
        'income': income,
        'page_obj': page_obj,
        'currency': currency,
        
    }
    return render(request, 'income/index.html', context)


@login_required(login_url='/authentication/login')
def add_income(request):
      owner_id = User.objects.filter(username=request.user).values_list('id', flat=True).first()
      print(owner_id)
      sources = Source.objects.filter(owner_id=owner_id)

      

      owner_id = User.objects.filter(username=request.user).values_list('id', flat=True).first()
      print(owner_id)
      sources = Source.objects.filter(owner_id=owner_id)


 
      context={
        'sources':sources,
        'values':request.POST
      }
      if request.method=='GET':
            return render(request,'income/add_income.html',context)

      if request.method=="POST":
            amount=request.POST['amount']
            if not amount:
                 messages.error(request,"Amount is required")
                 return render(request,'income/add_income.html')
            
            description=request.POST['description']
            date=request.POST['income_date']
            source=request.POST['source']


            if not description:
                 messages.error(request,'description is required')                 
                 return render(request,'income/add_income.html')
            
            UserIncome.objects.create(owner=request.user,
                                      amount=amount,
                                      date=date,
                                      source=source,
                                      description=description
                                      )
            messages.success(request,"Record saved successfully")
            return redirect("show_income")
            




            return render(request,'income/add_income.html',context)


@login_required(login_url='/authentication/login')      
def edit_income(request,id):
    
      income=UserIncome.objects.get(pk=id)
      sources=Source.objects.all()
      context={
            'income':income,
            'values':income,
            'source':sources
      }

      if request.method=='GET':
            return render(request, 'income/edit_income.html',context)
    
      if request.method=='POST':
            amount=request.POST['amount']
            if not amount:
                  messages.error(request,"amount is required")
                  return render(request,'userincome/edit_income.html',context)
            
            description = request.POST['description']
            date = request.POST['income_date']
            source = request.POST['source']
            
            if not description:
                  messages.error(request, 'description is required')
                  return render(request, 'income/edit_income.html', context)
            
            income.amount = amount
            income. date = date
            income.source = source
            income.description = description
            income.save()
            messages.success(request, 'Record updated  successfully')

            return redirect('show_income')





         
    


      return HttpResponse(f"you can edit your income here={id}")


@login_required(login_url='/authentication/login')
def delete_income(request,id):

      income=UserIncome.objects.get(pk=id)
      income.delete()
      messages.success(request,"income removed")
      return redirect ("show_income")

       
