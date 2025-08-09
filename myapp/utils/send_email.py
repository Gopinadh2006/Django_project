from django.core.mail import send_mail
import random

def send_otp_email(email):
    otp = random.randint(10000,99999)
    subject = 'Your OTP Code'
    message = 'f Your OTP is :{otp}'
    from_email = None
    send_mail = (subject, message, from_email, [email])
    return otp