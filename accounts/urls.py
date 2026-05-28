from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    path('blog/', views.blog, name='blog'),
    path('blog/<int:id>/', views.blog_details, name='blog_details'),
]