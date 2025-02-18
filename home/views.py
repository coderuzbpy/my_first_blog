from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home/home.html')

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
        else:
            print(form.errors)  # Xatoliklarni tekshirish
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def my_login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profile')  # Profil sahifasiga yo'naltirish
        else:
            return HttpResponse("Login yoki parol xato!")
    return render(request, 'login.html')

@login_required
def profile(request):
    return render(request, 'profile.html')
