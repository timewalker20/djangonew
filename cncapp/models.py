
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
Bloodgroup_choices = {
                ('AB+', 'AB POSITIVE'),
                ('AB-', 'AB NEGATIVE'),
                ('A+', 'A POSITIVE'),
                ('A-', 'A NEGATIVE'),
                ('B+', 'B POSITIVE'),
                ('B-', 'B NEGATIVE'),
                ('O+', 'O POSITIVE'),
                ('O-', 'O NEGATIVE'),
    }
Gender_choices = {
            ('Male', 'Male'),
            ('Female','Female')
           }  

User_type={
    ('Doctor','Doctor'),
    ('Patient','Patient'),
    ('Hospital','Hospital'),
    ('Pharmacist','Pharmacist'),
    ('Ambulance','Ambulance'),
}

class User(AbstractUser):
    usertype= models.CharField(max_length=30)
    phone_no = models.CharField(max_length = 13,unique=True)
    # videocall= models.BooleanField(default=False)
    otp = models.CharField(max_length=6,null=True,blank=True)
   
    

class Tempory(models.Model):
      phone_no = models.CharField(max_length = 13,unique=True)
      otp = models.CharField(max_length=6,null=True,blank=True)
      verified=models.BooleanField(default=False)
# class Patient(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
#     full_name = models.CharField(max_length=300,default="0")
#     email = models.EmailField(max_length=300,unique=True)
#     contactno = models.CharField( max_length=13,default="0")
#     pincode = models.CharField(max_length = 10,default="0")
#     disease = models.TextField(max_length=300,blank=False)
#     aadhaarno = models.CharField(max_length=12,default="0")
#     emergency = models.TextField(max_length=400,blank=False,null=True)
#     gender = models.CharField(max_length=10,blank=False,default="0")
#     bloodgroup = models.CharField(max_length=15,blank=False,default="0")
#     def __str__(self):
#         return self.full_name


class Doctor(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    full_name= models.CharField(max_length=300,default="0")
    email = models.EmailField(max_length=300,unique=True)
    desc = models.TextField(max_length=400,blank=False,null=True)
    services= models.TextField(max_length=400,blank=False,null=True)
    doctorimage = models.ImageField(blank=True, upload_to='doctor_pics',null=True)
    contactno = models.CharField(max_length=13,default="0",unique=True)
    address=models.CharField(max_length=200,blank=False,null=True)
    city = models.CharField(max_length=20,default="0")
    pincode = models.CharField(max_length = 6,default="0")
    experience = models.CharField(max_length=20,blank=False)
    speciality = models.CharField(max_length=20,blank=False)
    gender = models.CharField(max_length=10,blank=False,default="0")
    amount= models.FloatField(blank=False,default=0.0,null=True)
    
    def __str__(self):
        return self.full_name

class Pathologist(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    full_name= models.CharField(max_length=300,default="0")
    email = models.EmailField(max_length=300,unique=True)
    desc = models.TextField(max_length=400,blank=False,null=True)
    services= models.TextField(max_length=400,blank=False,null=True)
    pathologistimage = models.ImageField(blank=True, upload_to='pathologist_pics',null=True)
    contactno = models.CharField(max_length=13,default="0",unique=True)
    address=models.CharField(max_length=200,blank=False,null=True)
    city = models.CharField(max_length=20,default="0")
    pincode = models.CharField(max_length = 6,default="0")
    experience = models.CharField(max_length=20,blank=False)
    speciality = models.CharField(max_length=20,blank=False)
    gender = models.CharField(max_length=10,blank=False,default="0")
    amount= models.FloatField(blank=False,default=0.0,null=True)
    
    def __str__(self):
        return self.full_name

class HospitalDoctor(models.Model):
    doctorname = models.CharField(max_length=100,blank=False)
    speciality = models.CharField(max_length=200,blank=False)
    experience = models.CharField(max_length=200,blank=False)
    doctorintroduction = models.CharField(max_length=200)

    def __str__(self):
        return self.doctorname


class Hospital(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    hospitalname = models.CharField(max_length=100,unique=True,blank=False)
    hospitalimage = models.ImageField(blank=True, upload_to='hospital_pics',null=True)
    email = models.EmailField(max_length=300,unique=True,)
    administratorname = models.CharField(max_length=100,blank=False,unique=True)
    desc = models.TextField(max_length=400,blank=False,null=True)
    contact_no = models.CharField(max_length=13,default="0",unique=True,blank=False,null=True)
    pincode = models.CharField(max_length = 10)
    city = models.CharField(max_length=20,default="0")
    address=models.CharField(max_length=200,blank=False,null=True)
    administratorname = models.CharField(max_length=100,blank=False,unique=True)
    facilities = models.TextField(max_length=400,blank=False,null=True)
    amount= models.FloatField(blank=False,default=0.0,null=True)

    def __str__(self):
        return self.hospitalname



class Pharmacist(models.Model):
     user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
     shop_name = models.CharField(max_length=200,blank=False,unique=True)
     shop_address = models.TextField(max_length=400,blank=False)
     phar_name = models.CharField(max_length=200,blank=False)
     email_pharm = models.EmailField( max_length=254,blank=False,unique=True)
     contact_no = models.CharField(max_length=13,blank=False,unique=True,null=True,default="0")
     pincode = models.CharField(max_length = 10,default="0")
     start_time = models.TimeField(default=0)
     end_time= models.TimeField(default=0)
    
     def __str__(self):
         return self.shop_name


class Inventory(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,unique=False)
    Pharmacist=models.ForeignKey(Pharmacist,on_delete=models.CASCADE,null=True)
    medicinename = models.CharField(max_length=200,blank=False)
    medicineimage = models.ImageField(blank=True, upload_to='medicine_pics')
    desc = models.TextField(max_length=400,blank=False,null=True)
    price = models.CharField(max_length=50,default="0")
    mfg_date = models.DateField(blank=False,null=True)
    exp_date = models.DateField(blank=False,null=True)
    medavailable= models.BooleanField(default=True)

    def __str__(self):
        return (self.medicinename)

class Driver(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    driver_name = models.CharField(max_length=300,blank=False,unique=False)
    contact_no = models.CharField(max_length=10,default="0",unique=True)
    aadhaarno = models.CharField(max_length=12,default="0",unique=True)

    def __str__(self):
        return (self.driver_name)

class Ambulance(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    Ambulanceimage = models.ImageField(blank=True, upload_to='ambulance_pics',null=True)
    company=models.CharField(max_length=200,blank=False)
    desc = models.TextField(max_length=400,blank=False,null=True)
    contact_no = models.CharField(max_length=13,default="0",unique=True,blank=False,null=True)
    city = models.CharField(max_length=20,default="0")
    address=models.CharField(max_length=200,blank=False,null=True)
    pincode = models.CharField(max_length = 10)
    amount= models.FloatField(blank=False,default=0.0,null=True)
    def __str__(self):
        return self.company

#//////-------- datashare-------////////
class PathologyDatashare(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,unique=False)
    pathologist= models.ForeignKey(Pathologist, on_delete=models.CASCADE)    
    full_name = models.CharField(max_length=300,default="0")
    email = models.EmailField(max_length=300)
    contactno = models.CharField( max_length=13,default="0")
    disease = models.TextField(max_length=300,blank=False)
    aadhaarno = models.CharField(max_length=12,default="0")
    emergency = models.TextField(max_length=400,blank=False,null=True)
    gender = models.CharField(max_length=10,blank=False,default='M')
    bloodgroup = models.CharField(max_length=15,blank=False,default='B+')
    accept= models.BooleanField(default=False)
    time= models.CharField(max_length=50,default="0")
    prescription=models.TextField(null=True)
    rtc=models.TextField(null=True)
    uid=models.IntegerField(default = 0)
    complete=models.BooleanField(default=False)
    channelName=models.CharField(max_length=50,default=" ")
    paid=models.BooleanField(default=False)
    current=models.BooleanField(default=True)
    def __str__(self):
        return self.full_name


class Datashare(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,unique=False)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)    
    full_name = models.CharField(max_length=300,default="0")
    email = models.EmailField(max_length=300,)
    contactno = models.CharField( max_length=13,default="0")
    disease = models.TextField(max_length=300,blank=False)
    aadhaarno = models.CharField(max_length=12,default="0")
    emergency = models.TextField(max_length=400,blank=False,null=True)
    gender = models.CharField(max_length=10,blank=False,default='M')
    bloodgroup = models.CharField(max_length=15,blank=False,default='B+')
    accept= models.BooleanField(default=False)
    time= models.CharField(max_length=50,default="0")
    date=models.CharField(max_length=50,default="0")
    complete=models.BooleanField(default=False)
    current=models.BooleanField(default=True)
    
    def __str__(self):
        return self.full_name


class AmbulnceDatashare(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,unique=False)
    Ambulance= models.ForeignKey(Ambulance, on_delete=models.CASCADE)    
    full_name = models.CharField(max_length=300,default="0")
    email = models.EmailField(max_length=300)
    contactno = models.CharField( max_length=13,default="0")
    disease = models.TextField(max_length=300,blank=False)
    aadhaarno = models.CharField(max_length=12,default="0")
    emergency = models.TextField(max_length=400,blank=False,null=True)
    gender = models.CharField(max_length=10,blank=False,default='M')
    bloodgroup = models.CharField(max_length=15,blank=False,default='B+')
    accept= models.BooleanField(default=False)
    longitude=models.FloatField(blank=False,default=0.0,null=True)
    latitude=models.FloatField(blank=False,default=0,null=True)
    time= models.CharField(max_length=50,default="0")
   
    def __str__(self):
        return self.full_name

class DocDatashare(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,unique=False)
    Doctor= models.ForeignKey(Doctor, on_delete=models.CASCADE)    
    full_name = models.CharField(max_length=300,default="0")
    email = models.EmailField(max_length=300)
    contactno = models.CharField( max_length=13,default="0")
    disease = models.TextField(max_length=300,blank=False)
    aadhaarno = models.CharField(max_length=12,default="0")
    emergency = models.TextField(max_length=400,blank=False,null=True)
    gender = models.CharField(max_length=10,blank=False,default='M')
    bloodgroup = models.CharField(max_length=15,blank=False,default='B+')
    accept= models.BooleanField(default=False)
    timeofshare= models.CharField(max_length=50,default="0")
    prescription=models.TextField(null=True)
    rtc=models.TextField(null=True)
    uid=models.IntegerField(default = 0)
    complete=models.BooleanField(default=False)
    channelName=models.CharField(max_length=50,default=" ")
    paid=models.BooleanField(default=False)
    current=models.BooleanField(default=True)
    def __str__(self):
        return self.full_name


    
# Create your models here.

class Booking(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,unique=False)
    Doctor= models.ForeignKey(Doctor,on_delete=models.CASCADE) 
    accepted= models.BooleanField(default=False) 
    booking_amount = models.CharField(max_length=25)
    booking_payment_id = models.CharField(max_length=100)
    isPaid = models.BooleanField(default=False)
    date = models.DateField(default=0)
    start_time = models.TimeField(default=0)
    
class PathologyBooking(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,unique=False)
    pathologist= models.ForeignKey(Pathologist,on_delete=models.CASCADE) 
    accepted= models.BooleanField(default=False) 
    booking_amount = models.CharField(max_length=25)
    booking_payment_id = models.CharField(max_length=100)
    isPaid = models.BooleanField(default=False)
    date = models.DateField(default=0)
    start_time = models.TimeField(default=0)



#ecom
class Order ( models.Model ) :
    user = models.ForeignKey ( User , on_delete = models . SET_NULL , null = True , blank = True )
    Pharmacist=models.ForeignKey ( Pharmacist  , on_delete = models . SET_NULL , null = True , blank = True )
    date_ordered = models.DateTimeField ( auto_now_add = True )
    order_amount = models.CharField(max_length=25,default='0')
    order_payment_id = models.CharField(max_length=100,default="0")
    isPaid = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    complete = models . BooleanField ( default = False )
    status = models . CharField ( max_length = 100 , default="Pending")
    def _str_ ( self ) :
        return str ( self.id)
        
    # @property
    # def get_cart_total( self ):
    #     orderitems = self.orderitem_set.all( )  # type: ignore
    #     total = sum ( [ item.get_total for item in orderitems ] )
    #     return total

    # @property
    # def get_cart_items ( self ) :
    #     Iorderitems = self.orderitem_set.all( )
    #     total = sum ( [ item.quantity for item in Iorderitems ] )
    #     return total

class Orderitem ( models.Model ) :
    user= models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,unique=False)
    order = models . ForeignKey ( Order , on_delete = models . SET_NULL , null = True, blank = True )
    product = models . ForeignKey ( Inventory, on_delete = models . SET_NULL , null = True , blank = True)
    quantity = models . IntegerField ( default = 0 , null = True , blank = True ) 
    active=models.BooleanField(default=True)


    
    @property
    def get_total (self) :
        total = Inventory.price*self.quantity  # type: ignore
        return total




class ShippingAddress ( models.Model ) :
    user = models . ForeignKey (User,on_delete = models.SET_NULL , null = True )
    order = models . ForeignKey ( Order , on_delete = models . SET_NULL , null = True )
    address = models . CharField ( max_length = 200 , null = False )
    city = models . CharField ( max_length = 200 , null = False )
    state = models . CharField ( max_length = 200 , null = False )
    zipcode = models . CharField ( max_length = 200 , null = False )
    date_added = models.DateTimeField ( auto_now_add = True )
    def _str_ ( self ) :
        return self.address

