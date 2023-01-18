from django.core.mail import send_mail
import random
from django.conf import settings
from .models import *
import os
from twilio.rest import Client
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

def send_otp_login(phone):
 otp= random.randint(1000,9999)  
 account_sid = 'ACb26d3f1c466b71fc649287f7673dc1b2'
 auth_token = 'b27197a3aa0a7d2b345c7aeffca75bc4'
 client = Client(account_sid, auth_token)

 message = client.messages.create(
                     body= f"Your otp is {otp}",
                     from_='+16089245377',
                     to=phone
                     )
 print(message.sid)
 user_obj = User.objects.get(phone_no=phone)
 user_obj.otp = otp
 user_obj.save()

def send_otp_phone(phone):
 otp= random.randint(1000,9999)  
 account_sid = 'ACb26d3f1c466b71fc649287f7673dc1b2'
 auth_token = 'b27197a3aa0a7d2b345c7aeffca75bc4'
 client = Client(account_sid, auth_token)

 message = client.messages.create(
                     body= f"Your otp is {otp}",
                     from_='+16089245377',
                     to=phone
                     )
 print(message.sid)
 user_obj = Tempory.objects.get(phone_no=phone)
 user_obj.otp = otp
 user_obj.save()

