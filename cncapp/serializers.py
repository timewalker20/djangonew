
from dataclasses import field
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .models import *


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ['phone_no','username','usertype','dob']

    
    def create(self,validated_data):
         phone_no=validated_data.get('phone_no')
         user=User(phone_no=phone_no)
         user.save()
         return user

class VerifySerializer(serializers.Serializer):
    email= serializers.EmailField()
    otp= serializers.CharField()       
    
      
class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ['id','phone_no','username','usertype','dob']
    




# class PatientSerializer(serializers.ModelSerializer):
#     # user=serializers.HiddenField(default=serializers.CurrentUserDefault())
#     class Meta:
#         model = Patient
#         fields = '__all__'




class MedSerializer(serializers.ModelSerializer):
    user=serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Inventory
        fields = '__all__'

        

class PharmaSerializer(serializers.ModelSerializer):
    #user=serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Pharmacist
        fields = '__all__'

#hospital

class PatientDatashareSerializer(serializers.ModelSerializer):
    #  user=serializers.HiddenField(default=serializers.CurrentUserDefault())
     class Meta:
         model=Datashare
         fields='__all__'

class hospitalDatashareSerializer(serializers.ModelSerializer):
     class Meta:
         model=Datashare
         fields='__all__'

#ambulance

class PatientAmbDatashareSerializer(serializers.ModelSerializer):
     user=serializers.HiddenField(default=serializers.CurrentUserDefault())
     class Meta:
         model=AmbulnceDatashare
         fields='__all__'

class AmbulanceDatashareSerializer(serializers.ModelSerializer):
     class Meta:
         model=AmbulnceDatashare
         fields='__all__'

         

#doc
class PatientdocDatashareSerializer(serializers.ModelSerializer):
     #user=serializers.HiddenField(default=serializers.CurrentUserDefault())
     class Meta:
         model=DocDatashare
         fields='__all__' 
         
class DocDatashareSerializer(serializers.ModelSerializer):
     class Meta:
         model=DocDatashare
         fields='__all__'

class updocDatashareSerializer(serializers.ModelSerializer):
     class Meta:
         model=DocDatashare
         fields='__all__'

class bookingSerializer(serializers.ModelSerializer):
     class Meta:
         model=Booking
         fields='__all__'

#pathology--
class PatientpathologyDatashareSerializer(serializers.ModelSerializer):
     user=serializers.HiddenField(default=serializers.CurrentUserDefault())
     class Meta:
         model=PathologyDatashare
         fields='__all__'

class pathDatashareSerializer(serializers.ModelSerializer):
     class Meta:
         model=PathologyDatashare
         fields='__all__'

class uppathDatashareSerializer(serializers.ModelSerializer):
     class Meta:
         model=PathologyDatashare
         fields='__all__'

class PathbookingSerializer(serializers.ModelSerializer):
     class Meta:
         model=PathologyBooking
         fields='__all__'



#buyindmed

class  Orderitemserializer(serializers.ModelSerializer):
    class Meta:
        model=Orderitem
        fields='__all__'
        depth=1
       
class  GETOrderitemserializer(serializers.ModelSerializer):
    class Meta:
        model=Orderitem
        fields='__all__'
        depth=1
        
class  Orderserializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields='__all__'

class ShippingAddressserializer(serializers.ModelSerializer):
    class Meta:
        model=ShippingAddress 
        fields='__all__'


class PhramaorderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields='__all__'
        
       












class docotorSerializer(serializers.ModelSerializer):
    # user=serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Doctor
        fields = '__all__'

class pathologistSerializer(serializers.ModelSerializer):
    # user=serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Pathologist
        fields = '__all__'

class hospitaldoctorSerializer(serializers.ModelSerializer):
    # user=serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = HospitalDoctor
        fields = '__all__'

class hospitalSerializer(serializers.ModelSerializer):
    # user=serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Hospital
        fields = '__all__'

class AmbulanceSerializer(serializers.ModelSerializer):
    # user=serializers.HiddenField(default=serializers.CurrentUserDefault()) 
    class Meta:
        model = Ambulance
        fields = '__all__'
        
class driverSerializer(serializers.ModelSerializer):
    # user=serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Driver
        fields = '__all__'
