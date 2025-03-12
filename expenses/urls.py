from django.urls import path,include

from expenses import category_views
from . import views

from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
      
     path('', views.index, name="expenses"),
     path('add_expense', views.add_expense, name="add_expenses"),
     path('edit_expense/<int:id>', views.expense_edit, name="expense_edit"),
     path('expense_delete/<int:id>', views.delete_expense, name="expense_delete"),
     path('search_expenses', csrf_exempt(views.search_expenses),
         name="search_expenses"),
     path('expense_category_summary', views.expense_category_summary,
         name="expense_category_summary"),
     path('stats', views.stats_view,
         name="stats"),

 

     path('create_category',category_views.CategoryCreate.as_view(),name='create_category'),
     path('view_category',category_views.CategoryRetrieve.as_view(),name='view_category'),
     path('update_category/<int:pk>',category_views.CategoryUpdate.as_view(),name='update_category'),
     path('delete_category/<int:pk>',category_views.CategoryDelete.as_view(),name='delete_category'),





]
