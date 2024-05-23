from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('blog/', views.blog, name='blog'),     
    path('sign-up/', views.signup, name='sign-up'),
    path('log-in/',views.loginPage,name="log-in"),
    path('create/',views.create,name="create"),
    path('delete_post/<int:post_id>/',views.delete_post, name='delete_post'),
    path('trending/',views.trending,name="trending"),
    path('read-more/<int:post_id>/',views.readmore,name="read-more"),
    path('profile/',views.profile,name="profile"),
    path('updatepost/<int:post_id>/', views.updatepost, name='updatepost'),
    
]