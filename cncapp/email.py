from django.core.mail import send_mail
import random
from django.conf import settings
from .models import User
def send_otp_email(email):
    subject = 'Your Email Verification '
    otp= random.randint(1000,9999)
    message= f'Your OTP For Email Verification {otp}'
    email_form=settings.EMAIL_HOST
    send_mail(subject,message, email_form ,[email])
    user_obj = User.objects.get(email=email)
    user_obj.otp = otp
    user_obj.save()

def send_otp_password(email):
    subject = 'Forget Password '
    otp= random.randint(1000,9999)
    message= f'Your OTP For Password Reset {otp}'
    email_form=settings.EMAIL_HOST
    send_mail(subject,message, email_form ,[email])
    user_obj = User.objects.get(email=email)
    user_obj.otp = otp
    user_obj.save()