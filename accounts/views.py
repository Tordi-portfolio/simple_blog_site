from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # 🔴 Check username exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists . . .')
            return redirect('register')
        # 🔴 Check email exists (NEW FIX)
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists . . .')
            return redirect('register')
        # CREATE USER
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        messages.success(request, 'Account created successfully')
        return redirect('login')
    return render(request, 'register.html')


def user_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('login')


from django.shortcuts import render, get_object_or_404
from .models import Blog


def blog(request):

    blogs = Blog.objects.all().order_by('-created_at')

    context = {
        'blogs': blogs
    }

    return render(request, 'blog.html', context)


def blog_details(request, id):

    single_blog = get_object_or_404(Blog, id=id)

    context = {
        'blog': single_blog
    }

    return render(request, 'blog_details.html', context)