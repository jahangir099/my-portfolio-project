from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register_view, name='register_page'),
    path('login/', views.login_view, name='login_page'),
    path('profile/', views.profile_view, name='profile_page'),
    
    
]
