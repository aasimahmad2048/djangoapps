from django.urls import path
from income import source_views, views

from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('show_income',views.index,name="show_income"),
    path("add_income",views.add_income,name="add_income"),
    path("edit_income/<int:id>",views.edit_income,name="edit_income"),
    path("delete_income/<int:id>",views.delete_income,name="delete_income"),
    path('search_income', csrf_exempt(views.search_income),name="search_income"),




     path('create_source',source_views.SourceCreate.as_view(),name='create_source'),
     path('view_source',source_views.SourceRetrieve.as_view(),name='view_source'),
     path('update_source/<int:pk>',source_views.SourceUpdate.as_view(),name='update_source'),
     path('delete_source/<int:pk>',source_views.SourceDelete.as_view(),name='delete_source'),








]
