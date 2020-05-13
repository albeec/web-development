from django.urls import path
from . import views

urlpatterns = [
 	path('', views.blog_post_list),
    path('<str:slug>/', views.blog_post_detail),
    path('<str:slug>/update', views.blog_post_update),
    path('<str:slug>/delete', views.blog_post_delete)
]