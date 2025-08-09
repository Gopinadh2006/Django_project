from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('login/', auth_views.LoginView.as_view(template_name='myapp/login.html'), name='login'),  # Use the built-in LoginView
    path('home/', views.home_view, name='home'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Use the built-in LogoutView
    path('', views.home_view, name='home'),
     path('', views.get_email_view, name='get_email'),
    path('verify-otp/', views.verify_otp_view, name='verify_otp'),  # use this name in redirect()
]





