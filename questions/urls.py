from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_question, name='add_question'),
    path('', views.list_questions, name='list_questions'),
    path('edit/<int:pk>/', views.edit_question, name='edit_question'),
    path('delete/<int:pk>/', views.delete_question, name='delete_question'),
]
