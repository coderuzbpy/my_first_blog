"""
URL configuration for project_name project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from home import views
from customer.views import get_customer
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),  # Bosh sahifa
    path('login/', views.my_login_view, name='login'),  # Login sahifasi
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),  # Logout sahifasi
    path('register/', views.register, name='register'),  # Ro'yxatdan o'tish
    path('profile/', views.profile, name='profile'),  # Profil sahifasi
    path('customer/', get_customer, name='customer')
]

