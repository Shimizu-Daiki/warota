from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.get_create_form, name='form'),
    path("post/<int:pk>/delete/", views.delete, name="delete")
]