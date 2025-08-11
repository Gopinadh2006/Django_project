from django.shortcuts import render, redirect
from django.contrib.auth import logout
from myapp.utils.send_email import send_otp_email



def dashboard_view(request):
    return render(request, 'myapp/dashboard.html')

def login_view(request):
    return render(request, 'myapp/login.html')

def home_view(request):
    return render(request, 'myapp/home.html') 

def logout_view(request):
    logout(request)
    return redirect('login')

def home(request):
    return render(request, 'myapp/home.html')
    

def get_email_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        otp = send_otp_email(email)  # 🛠️ FIX: Call the function, don't assign it directly
        request.session['otp'] = otp
        request.session['email'] = email

        return redirect('verify_otp')  # ✅ FIX: use the URL **name** from urls.py

    return render(request, 'myapp/get_email.html')

from django.contrib import messages

def verify_otp_view(request):
    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        session_otp = request.session.get('otp')

        if entered_otp == session_otp:
            return render(request, 'myapp/success.html')  # Create this template if needed
        else:
            messages.error(request, 'Invalid OTP. Please try again.')

    return render(request, 'myapp/verify_otp.html')





