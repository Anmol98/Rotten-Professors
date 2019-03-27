from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.branch_list, name='branch_list'),
    path('list/<str:branch>/', views.prof_list_branch, name='prof_list_branch'),
    path('list/<str:bran>/<int:pk>/', views.prof_detail, name='prof_detail'),
    path('list/<str:bran>/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
