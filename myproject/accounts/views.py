from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
from .forms import CustomUserCreationForm
from django.contrib import messages
from .models import Profile


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data.get('email')
            user.save()

            full_name = form.cleaned_data.get('full_name')
            phone = form.cleaned_data.get('phone')
            Profile.objects.create(user=user, full_name=full_name, phone=phone)

            messages.success(request, "Registration successful! You can now log in.")
            return redirect('login_page')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register_page.html', {'form': form})







def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('profile_page')
        else:
            messages.error(request, "Invalid username or password.")
    
    return render(request, 'accounts/login_page.html', {'form': form})




def profile_view(request):
    return render(request, 'accounts/profile_page.html', {'user': request.user})
    
    

def logout_view(request):
    logout(request)
    return redirect('login_page')