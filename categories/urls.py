from django.urls import path
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from .models import Category

category_fields = ['name', 'description', 'image', 'parent']

app_name = 'categories'
urlpatterns = [
    path('', ListView.as_view(model=Category), name="category_list",),
    path('detail/<int:pk>', DetailView.as_view(model=Category), name="category_detail"),
    path('update/<int:pk>', UpdateView.as_view(model=Category), name="category_update"),
    path('delete/<int:pk>', DeleteView.as_view(model=Category, success_url='/'), name="category_delete"),
    path('create/', CreateView.as_view(model=Category, fields = category_fields), name="category_create"),
]
