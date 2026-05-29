from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    path('blog/', views.blog, name='blog'),
    path('blog/<int:id>/', views.blog_details, name='blog_details'),

    # RESET PASSWORD

    path(
        'reset_password/',
        auth_views.PasswordResetView.as_view(
            template_name='reset/reset_password.html'
        ),
        name='reset_password'
    ),

    path(
        'reset_password_sent/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='reset/reset_password_sent.html'
        ),
        name='password_reset_done'
    ),

    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='reset/reset_password_form.html'
        ),
        name='password_reset_confirm'
    ),

    path(
        'reset_password_complete/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='reset/reset_password_done.html'
        ),
        name='password_reset_complete'
    ),

]