from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from myapp import views  # Import views from your app, not the project


urlpatterns = [
     path('home/', views.home_view, name='home'), 
    # Admin panel URL
    path('admin/', admin.site.urls),  # This will enable the Django admin panel
   


    # Your app URLs
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('home/', views.home_view, name='home'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.home_view, name='home'),
    path('', include('myapp.urls')),
]

