from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.branch_list, name='branch_list'),
    path('post/<str:pk>/', views.prof_list_branch, name='prof_list_branch')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
