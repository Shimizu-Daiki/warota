from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.get_create_form, name='form'),
    path("post/<int:pk>/delete/", views.delete, name="delete"),
    path("post/<int:pk>/show/", views.show, name="show"),
    path('answer', views.get_answer_form, name='answer'),
    path("answer/<int:pk>/delete/", views.answer_delete, name="answer_delete"),
    path("answer/<int:pk>/delete/", views.answer_delete, name="answer_delete"),
    path('swap_word/<int:pk>/show/', views.swap_word, name='ai_answer'),
]