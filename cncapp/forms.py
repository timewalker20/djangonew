from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import Doctor,User,Pharmacist,Hospital,Patient,Inventory,Driver,Ambulance,Patient,BloodGroup,Gender

class PatientsignupForm(ModelForm):
    class Meta():
        model = Patient
        fields = ('first_name','last_name','gender','bloodgroup','email','contactno','pincode','disease','aadhaarno','emergency')
        bloodgroup = forms.ModelChoiceField(queryset=BloodGroup.objects.all())
        gender = forms.ModelChoiceField(queryset=Gender.objects.all())
        # hospital = forms.ModelChoiceField(queryset=Hospital.objects.all())
        # doctor = forms.ModelChoiceField(queryset=Doctor.objects.all())
        # pharmacist = forms.ModelChoiceField(queryset=Pharmacist.objects.all())
        # ambulance = forms.ModelChoiceField(queryset=Ambulance.objects.all())


# class UsersignupForm(UserCreationForm):
#     first_name = forms.CharField(max_length=300,required=True)
#     last_name = forms.CharField(max_length=300,required=True)
#     email_ID = forms.EmailField( max_length=254,required=True)
    # CHOICES = (
    #     ('type', 'AB+'),
    #     ('type', 'AB-'),
    #     ('type', 'A+'),
    #     ('type', 'A-'),
    #     ('type', 'B+'),
    #     ('type', 'B-'),
    #     ('type', 'O+'),
    #     ('type', 'O-'),
    #     )
    # bloodgroup = forms.CharField(widget=forms.Select(choices=CHOICES), required=True)
#     pincode = forms.IntegerField(required=True)
#     contact_no = forms.IntegerField(required=True)
#     aadhaarno = forms.IntegerField(required=True)
#
#     class Meta(UserCreationForm.Meta):
#         model = User
#
#     @transaction.atomic
#     def save(self):
#         user = super().save(commit=False)
#         user.is_user=True
#         user.save()
#         user = ApplicationUser.objects.create(user=user)
#         user.first_name = self.cleaned_data.get('first_name')
#         user.last_name = self.cleaned_data.get('last_name')
#         user.email_ID = self.cleaned_data.get('email_ID')
#         user.bloodgroup = self.cleaned_data.get('bloodgroup')
#         user.pincode = self.cleaned_data.get('pincode')
#         user.contact_number = self.cleaned_data.get('contact_number')
#         user.aadhaarno = self.cleaned_data.get('aadhaarno')
#         user.save()
#         return user

class DoctorsignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=300)
    last_name = forms.CharField(max_length=300)
    email = forms.EmailField(max_length=300,required=True)
    # password = forms.CharField(max_length=8,required=True)
    contactno = forms.IntegerField(required=True)
    pincode = forms.IntegerField(required=True)
    experience = forms.CharField(max_length=400,required=True)
    speciality = forms.CharField(max_length=300,required=True)


    class Meta(UserCreationForm.Meta):

        model = User

    @transaction.atomic
    def save(self):
            user = super().save(commit=False)
            user.is_doctor=True
            # user.first_name = self.cleaned_data.get('first_name')
            # user.last_name = self.cleaned_data.get('last_name')
            user.save()
            doctor = Doctor.objects.create(user=user)
            doctor.first_name = self.cleaned_data.get('first_name')
            doctor.last_name = self.cleaned_data.get('last_name')
            doctor.email = self.cleaned_data.get('email')
            # doctor.password = self.cleaned_data.get('password')
            doctor.contactno = self.cleaned_data.get('contactno')
            doctor.pincode = self.cleaned_data.get('pincode')
            doctor.experience = self.cleaned_data.get('experience')
            doctor.speciality = self.cleaned_data.get('speciality')
            doctor.save()
            return user

class PharmacistSignupForm(UserCreationForm):
      shop_name = forms.CharField(max_length=200,required=True)
      shop_address = forms.CharField(widget=forms.Textarea(attrs={"rows":5,"cols":5}))
      phar_name = forms.CharField(max_length=200,required=True)
      email_pharm = forms.EmailField(max_length=254,required=True)
      contact_no = forms.IntegerField(required=True)
      pincode = forms.IntegerField(required=True)

      class Meta(UserCreationForm.Meta):
         model=User

      @transaction.atomic
      def save(self):
            user = super().save(commit=False)
            user.is_pharmacist=True
            user.save()
            pharmacist = Pharmacist.objects.create(user=user)
            pharmacist.shop_name = self.cleaned_data.get('shop_name')
            pharmacist.shop_address = self.cleaned_data.get('shop_address')
            pharmacist.phar_name = self.cleaned_data.get('phar_name')
            pharmacist.email_pharm = self.cleaned_data.get('email_pharm')
            pharmacist.contact_no = self.cleaned_data.get('contact_no')
            pharmacist.pincode = self.cleaned_data.get('pincode')
            pharmacist.save()
            return user

class InventoryDetailForm(UserCreationForm):
    medicinename = forms.CharField(max_length=100,required=True)
    medicinepic = forms.ImageField()
    price = forms.FloatField(required=True)
    mfg_date = forms.DateField(widget=forms.SelectDateWidget)
    exp_date = forms.DateField(widget=forms.SelectDateWidget)
    class Meta(UserCreationForm.Meta):
      model = User
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_inventory=True
        user.save()
        inventory = Inventory.objects.create(user=user)
        inventory.medicinename = self.cleaned_data.get('medicinename')
        inventory.price = self.cleaned_data.get('price')
        inventory.mfg_date = self.cleaned_data.get('mfg_date')
        inventory.exp_date = self.cleaned_data.get('exp_date')

# class PharmacistSignupForm(ModelForm):
#     class Meta():
#         model = Pharmacist
#         fields = ('shop_name','shop_address','phar_name','email_pharm','contact_no','pincode')
        # patient = forms.ModelChoiceField(queryset=Patient.objects.all())
        # inventory = forms.ModelChoiceField(queryset=Inventory.objects.all())

class HospitalsignupForm(UserCreationForm):
    hospitalname = forms.CharField(max_length=100,required=True)
    contact_number = forms.IntegerField(required=True)
    pincode = forms.IntegerField(required=True)
    administratorname = forms.CharField(max_length=100,required=True)
    facilities = forms.CharField(widget=forms.Textarea(attrs={"rows":5,"cols":10}))
    ratings = forms.FloatField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_hospital=True
        user.save()
        hospital = Hospital.objects.create(user=user)
        hospital.hospitalname = self.cleaned_data.get('hospitalname')
        hospital.contact_number = self.cleaned_data.get('contact_number')
        hospital.pincode = self.cleaned_data.get('pincode')
        hospital.administratorname = self.cleaned_data.get('administratorname')
        hospital.facilities = self.cleaned_data.get('facilities')
        hospital.ratings = self.cleaned_data.get('ratings')
        hospital.save()
        return user

class DriverSignupForm(UserCreationForm):
    driver_name = forms.CharField(max_length=100,required=True)
    contact_no = forms.IntegerField(required=True)
    aadhaarno = forms.IntegerField(required=True)
    class Meta(UserCreationForm.Meta):
        model = User
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_driver=True
        user.save()
        driver = Driver.objects.create(user=user)
        driver.driver_name =  self.cleaned_data.get('driver_name')
        driver.contact_no =  self.cleaned_data.get('contact_no')
        driver.aadhaarno =  self.cleaned_data.get('aadhaarno')
        driver.save()
        return user


class AmbulanceDeatilForm(ModelForm):
    class Meta():
        model = Ambulance
        fields = ('vehicleno','areacode','driver')
        driver = forms.ModelChoiceField(queryset=Driver.objects.all())
