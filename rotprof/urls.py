from django.urls import path
from . import views

urlpatterns = [
    path('', views.branch_list, name='branch_list'),
    path('post/<str:pk>/', views.prof_list_branch, name='prof_list_branch')
]
