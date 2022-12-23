
from django.utils import timezone
import json
from django.shortcuts import render,get_object_or_404
import razorpay
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from knox.models import AuthToken
from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
#rzp_test_6KLtvINdjNoEpt
#r4R6mqiWSOBMxENvbVzHS5pa
#client
#rzp_test_8SYblYb1SY5Ixj
#s3ekF1bZRISt5IXjXNR6RtJi

from django.shortcuts import render
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest


# authorize razorpay client with API Keys.

# razorpay_client = razorpay.Client(
# 	auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))


# def homepage(request):
# 	currency = 'INR'
# 	amount = 20000 # Rs. 200

# 	# Create a Razorpay Order
# 	razorpay_order = razorpay_client.order.create(dict(amount=amount,
# 													currency=currency,
# 													payment_capture='0'))

# 	# order id of newly created order.
# 	razorpay_order_id = razorpay_order['id']
# 	callback_url = 'paymenthandler'

# 	# we need to pass these details to frontend.
# 	context = {}
# 	context['razorpay_order_id'] = razorpay_order_id
# 	context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
# 	context['razorpay_amount'] = amount
# 	context['currency'] = currency
# 	context['callback_url'] = callback_url

# 	return render(request, 'index.html', context=context)


# # we need to csrf_exempt this url as
# # POST request will be made by Razorpay
# # and it won't have the csrf token.
# @csrf_exempt
# def paymenthandler(request):

# 	# only accept POST request.
# 	if request.method == "POST":
# 		try:
		
# 			# get the required parameters from post request.
# 			payment_id = request.POST.get('razorpay_payment_id', '')
# 			razorpay_order_id = request.POST.get('razorpay_order_id', '')
# 			signature = request.POST.get('razorpay_signature', '')
# 			params_dict = {
# 				'razorpay_order_id': razorpay_order_id,
# 				'razorpay_payment_id': payment_id,
# 				'razorpay_signature': signature
# 			}

# 			# verify the payment signature.
# 			result = razorpay_client.utility.verify_payment_signature(
# 				params_dict)
# 			if result is not None:
# 				amount = 20000 # Rs. 200
# 				try:

# 					# capture the payemt
# 					razorpay_client.payment.capture(payment_id, amount)

# 					# render success page on successful caputre of payment
# 					return render(request, 'paymentsuccess.html')
# 				except:

# 					# if there is an error while capturing payment.
# 					return render(request, 'paymentfail.html')
# 			else:

# 				# if signature verification fails.
# 				return render(request, 'paymentfail.html')
# 		except:

# 			# if we don't find the required parameters in POST data
# 			return HttpResponseBadRequest()
# 	else:
# 	# if other than POST request is made.
# 		return HttpResponseBadRequest()



razorpay_client = razorpay.Client(
	auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))

@api_view(['POST'])
def homepage(request):
    currency="INR"
    user=request.data['user']
    doctor= int(request.data['Doctor'])
    #accepted= request.data['accepted']
    date = request.data['date']
    start_time = request.data['start_time']
    amount = request.data['amount']

	# Create a Razorpay Order
    razorpay_order = razorpay_client.order.create(dict(amount=int(amount) * 100,
													currency=currency,
													payment_capture='0'))

	# order id of newly created order.
    razorpay_order_id = razorpay_order['id']
    callback_url = 'paymenthandler'
    order = Booking.objects.create( 
                                 user= User.objects.get(id=user),
                                 Doctor=Doctor.objects.get(id=doctor),
                                # accepted=accepted,     
                                 booking_amount=int(amount) * 100, 
                                 date=date,
                                 start_time=start_time,
                                 booking_payment_id=razorpay_order_id)

    serializer =bookingSerializer(order)

	# we need to pass these details to frontend.
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url
    data={
        "payment": razorpay_order,
        "order": serializer.data,
        "context":context
    }
    return Response(data)

    # render(request, 'index.html', context=context)

# we need to csrf_exempt this url as
# POST request will be made by Razorpay
# and it won't have the csrf token.
@csrf_exempt
def paymenthandler(request):

	# only accept POST request.
	if request.method == "POST":
		try:
		
			# get the required parameters from post request.
			payment_id = request.POST.get('razorpay_payment_id', '')
			razorpay_order_id = request.POST.get('razorpay_order_id', '')
			signature = request.POST.get('razorpay_signature', '')
			params_dict = {
				'razorpay_order_id': razorpay_order_id,
				'razorpay_payment_id': payment_id,
				'razorpay_signature': signature
			}

			# verify the payment signature.
			result = razorpay_client.utility.verify_payment_signature(
				params_dict)
			if result is not None:
				amount = 20000 # Rs. 200
				try:

					# capture the payemt
					razorpay_client.payment.capture(payment_id, amount)

					# render success page on successful caputre of payment
					return render(request, 'paymentsuccess.html')
				except:

					# if there is an error while capturing payment.
					return render(request, 'paymentfail.html')
			else:

				# if signature verification fails.
				return render(request, 'paymentfail.html')
		except:

			# if we don't find the required parameters in POST data
			return HttpResponseBadRequest()
	else:
	# if other than POST request is made.
		return HttpResponseBadRequest()

































































































# @api_view(['POST'])
# def start_payment(request):
#     # request.data is coming from frontend
#     user= int(request.data['user'])
#     doctor= int(request.data['Doctor'])
#     accepted= request.data['accepted']
#     amount = request.data['amount']
#     date = request.data['date']
#     start_time = request.data['start_time']
#     # setup razorpay client this is the client to whome user is paying money that's you
#     client = razorpay.Client(auth=("rzp_test_8SYblYb1SY5Ixj", "s3ekF1bZRISt5IXjXNR6RtJi"))

#     # create razorpay order
#     # the amount will come in 'paise' that means if we pass 50 amount will become
#     # 0.5 rupees that means 50 paise so we have to convert it in rupees. So, we will 
#     # mumtiply it by 100 so it will be 50 rupees.
#     payment = client.order.create({"amount": int(amount) * 100, 
#                                    "currency": "INR", 
#                                    "payment_capture": "1"})

#     # we are saving an order with isPaid=False because we've just initialized the order
#     # we haven't received the money we will handle the payment succes in next 
#     # function
#     order = Booking.objects.create( 
#                                  user= User.objects.get(id=user),
#                                  Doctor=Doctor.objects.get(id=doctor),
#                                  accepted=accepted,     
#                                  booking_amount=int(amount) * 100, 
#                                  date=date,
#                                  start_time=start_time,
#                                  booking_payment_id=payment['id'])

#     serializer =bookingSerializer(order)

#     """order response will be 
#     {'id': 17, 
#     'order_date': '23 January 2021 03:28 PM', 
#     'order_product': '**product name from frontend**', 
#     'order_amount': '**product amount from frontend**', 
#     'order_payment_id': 'order_G3NhfSWWh5UfjQ', # it will be unique everytime
#     'isPaid': False}"""

#     data = {
#         "payment": payment,
#         "order": serializer.data
#     }
#     return Response(data)



# @api_view(['POST'])
# def handle_payment_success(request):
#     # request.data is coming from frontend
#     res = json.loads(request.data["response"])

#     """res will be:
#     {'razorpay_payment_id': 'pay_G3NivgSZLx7I9e', 
#     'razorpay_order_id': 'order_G3NhfSWWh5UfjQ', 
#     'razorpay_signature': '76b2accbefde6cd2392b5fbf098ebcbd4cb4ef8b78d62aa5cce553b2014993c0'}
#     this will come from frontend which we will use to validate and confirm the payment
#     """

#     ord_id = ""
#     raz_pay_id = ""
#     raz_signature = ""

#     # res.keys() will give us list of keys in res
#     for key in res.keys():
#         if key == 'razorpay_order_id':
#             ord_id = res[key]
#         elif key == 'razorpay_payment_id':
#             raz_pay_id = res[key]
#         elif key == 'razorpay_signature':
#             raz_signature = res[key]

#     # get order by payment_id which we've created earlier with isPaid=False
#     order = Booking.objects.get(order_payment_id=ord_id)

#     # we will pass this whole data in razorpay client to verify the payment
#     data = {
#         'razorpay_order_id': ord_id,
#         'razorpay_payment_id': raz_pay_id,
#         'razorpay_signature': raz_signature
#     }

#     client = razorpay.Client(auth=("rzp_test_8SYblYb1SY5Ixj", "r4R6mqiWSOBMxENvbVzHS5pa"))

#     # checking if the transaction is valid or not by passing above data dictionary in 
#     # razorpay client if it is "valid" then check will return None
#     check = client.utility.verify_payment_signature(data)

#     if check is not None:
#         print("Redirect to error url or error page")
#         return Response({'error': 'Something went wrong'})

#     # if payment is successful that means check is None then we will turn isPaid=True
#     order.isPaid = True
#     order.save()

#     res_data = {
#         'message': 'payment successfully received!'
#     }

#     return Response(res_data)


class getuserbooking(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    authentication_classes = [TokenAuthentication] 
    serializer_class = bookingSerializer
    def get_queryset(self):
        queryset = Booking.objects.filter(user=self.request.user)
        return  queryset


class getdocbooking(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    authentication_classes = [TokenAuthentication] 
    serializer_class = bookingSerializer
    def get_queryset(self):
        data = Doctor.objects.get(user=self.request.user)
        queryset = Booking.objects.filter(Doctor=data)  
        return  queryset
        
@api_view(['POST'])
def start_payment(request):
    # request.data is coming from frontend
    user= int(request.data['user'])
    doctor= int(request.data['Doctor'])
    accepted= request.data['accepted']
    amount = request.data['amount']
    date = request.data['date']
    start_time = request.data['start_time']
    value= request.data['value']
    print(value)
    if value == "true":
     order = Booking.objects.create( 
                                 user= User.objects.get(id=user),
                                 Doctor=Doctor.objects.get(id=doctor),
                                 accepted=accepted,     
                                 booking_amount=int(amount) * 100, 
                                 date=date,
                                 start_time=start_time,
                                 booking_payment_id=0
                                 )
     order.save()
     serializer =bookingSerializer(order)
     User.objects.filter(id=user).update(videocall=True)
     data = {
        "order": serializer.data,
        "message":"booking done"
       }
     return Response(data)
    else:
        return Response({"message":"payment is not successful"})
###Pathology###
class getuser_pathbooking(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    authentication_classes = [TokenAuthentication] 
    serializer_class = PathbookingSerializer
    def get_queryset(self):
        queryset = PathologyBooking.objects.filter(user=self.request.user)
        return  queryset

class getpath_booking(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    authentication_classes = [TokenAuthentication] 
    serializer_class = PathbookingSerializer
    def get_queryset(self):
        data = Pathologist.objects.get(user=self.request.user)
        queryset = PathologyBooking.objects.filter(Doctor=data)  
        return  queryset
        
@api_view(['POST'])
def start_payment_Pathology(request):
    # request.data is coming from frontend
    user= int(request.data['user'])
    pathologist= int(request.data['Patholgist'])
    accepted= request.data['accepted']
    amount = request.data['amount']
    date = request.data['date']
    start_time = request.data['start_time']
    value= request.data['value']
    print(value)
    if value == "true":
     order = PathologyBooking.objects.create( 
                                 user= User.objects.get(id=user),
                                 pathologist=Pathologist.objects.get(id=pathologist),
                                 accepted=accepted,     
                                 booking_amount=int(amount) * 100, 
                                 date=date,
                                 start_time=start_time,
                                 booking_payment_id=0
                                 )
     order.save()
     serializer =PathbookingSerializer(order)
     User.objects.filter(id=user).update(videocall=True)
     data = {
        "order": serializer.data,
        "message":"booking done"
       }
     return Response(data)
    else:
        return Response({"message":"payment is not successful"})

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def endcall(request):
    User.objects.filter(id=request.user.id).update(videocall=False)
    return Response({"message":"done"})

class profilepack(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    authentication_classes = [TokenAuthentication] 
    serializer_class = UserDetailSerializer
    def get_queryset(self):
        queryset = User.objects.filter(id=self.request.user.id)
        print(queryset)
        return  queryset



class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        if User.objects.filter(username=user,is_verified=True).exists():
         token, created = Token.objects.get_or_create(user=user)
         return Response({
            'token': token.key,
            'user_id': user.pk,
            'username':user.username,
            'full_name':user.full_name,
            'email': user.email,
            'usertype':user.usertype,
            'bloodgroup':user.bloodgroup,
            'gender':user.gender,
            'phone_no':user.phone_no if user.phone_no else '',
            'is_verified':user.is_verified
         })
        else:
            return Response({
                'status':333,
                'message':'Account Not Verified'

            })
from .email import *
# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        send_otp_email(serializer.data['email'])
        return Response({
        "user": UserDetailSerializer(user, context=self.get_serializer_context()).data
        })


class verifyOTP(APIView):
      def post(self,request):
        try:
            data= request.data
            serializer = VerifySerializer(data=data)

            if serializer.is_valid():
                email= serializer.data['email']
                otp = serializer.data['otp']
                user= User.objects.filter(email=email)
                if not user.exists():
                    return Response({
                        'status':400,
                        'message':'invaild email'
                    })
                if  user[0].otp != otp:
                    return Response({
                        'status':400,
                        'message':'wrong otp'
                     })  
                user = user.first()
                user.is_verified =True
                user.save()
                return Response({
                        'status':500,
                        'message':'verified'
                     }) 
            
        except Exception as e:
            print(e)

@api_view(['POST'])
def ForgetPassword(request):
     email=request.data["email"]
     if User.objects.filter(email=email).exists():
        send_otp_password(email)
        return Response({
            "message":"OTP Sent"
        })
     else:
        return Response({
            "message":"Email doesn't exsits"
        })    

@api_view(['POST'])
def PasswordReset(request):
     otp=request.data["otp"]
     newpassword=request.data['newpassword']
     if User.objects.filter(otp=otp).exists():
        User.objects.filter(otp=otp).update(password=newpassword)
        return Response({
            "message":" Password Reset Successfuly"
        })
     else:
        return Response({
            "message":"Wrong OTP "
        }) 


#private--pharma

class UserPharmaList(generics.ListCreateAPIView):
    # permission_classes=[IsAuthenticated]
    permission_classes=[IsAuthenticated]
    authentication_classes = [TokenAuthentication] 
    serializer_class = PharmaSerializer
    def get_queryset(self):
        queryset = Pharmacist.objects.filter(user=self.request.user)
        return  queryset
    def perform_create(self, serializer):
        serializer.save()

class UserMedtList(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    authentication_classes = [TokenAuthentication] 
    serializer_class = MedSerializer
    def get_queryset(self):
        queryset = Inventory.objects.filter(user=self.request.user)
        return  queryset


class UserMedDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventory.objects.all()
    serializer_class = MedSerializer

class UserpharmaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pharmacist.objects.all()
    serializer_class = PharmaSerializer


#private patient

class UserPatientList(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = PatientSerializer
    def get_queryset(self):
        queryset = Patient.objects.filter(user=self.request.user)
        return  queryset
   

class UserPatientDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes=[IsAuthenticated]
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()
   
    

#private doctor
class UserdoctorList(generics.ListCreateAPIView):
    # permission_classes=[IsAuthenticated]
    permission_classes=[IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = docotorSerializer
    def get_queryset(self):
        queryset = Pathologist.objects.filter(user=self.request.user)
        return  queryset
   

class UserdoctorDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes=[IsAuthenticated]
    queryset = Doctor.objects.all()
    serializer_class = docotorSerializer
    

#private pathology---
class UserPathologistList(generics.ListCreateAPIView):
    # permission_classes=[IsAuthenticated]
    permission_classes=[IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = pathologistSerializer
    def get_queryset(self):
        queryset = Pathologist.objects.filter(user=self.request.user)
        return  queryset

class UserPathologistDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes=[IsAuthenticated]
    queryset = Pathologist.objects.all()
    serializer_class = pathologistSerializer

#private hospital
class UserhospList(generics.ListCreateAPIView):
    # permission_classes=[IsAuthenticated]
    permission_classes=[IsAuthenticated]
    authentication_classes = [TokenAuthentication] 
    serializer_class = hospitalSerializer
    def get_queryset(self):
        queryset = Hospital.objects.filter(user=self.request.user)
        return  queryset
   

class UserhospDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hospital.objects.all()
    serializer_class = hospitalSerializer





class UserAmbulancelist(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = AmbulanceSerializer
    def get_queryset(self):
        queryset =Ambulance.objects.filter(user=self.request.user)
        return  queryset
   

class UserAmbulancedetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ambulance.objects.all()
    serializer_class = AmbulanceSerializer



# class driverlist(generics.ListCreateAPIView):
#     # permission_classes=[IsAuthenticated]
#     queryset = Driver.objects.all()
#     serializer_class = driverSerializer

# class driverDetail(generics.RetrieveUpdateDestroyAPIView):
#     # permission_classes=[IsAuthenticated]
#     queryset = Driver.objects.all()
#     serializer_class = driverSerializer


class getuserdatashare(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    authentication_classes = [TokenAuthentication] 
    serializer_class = PatientDatashareSerializer
    def get_queryset(self):
        queryset = Datashare.objects.filter(user=self.request.user)
        return  queryset

class updategetuserdatashare(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAuthenticated]
    authentication_classes = [TokenAuthentication] 
    queryset = Datashare.objects.all()
    serializer_class = PatientDatashareSerializer



class gethospitaldatashare(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    authentication_classes = [TokenAuthentication] 
    serializer_class = hospitalDatashareSerializer
    def get_queryset(self):
        data = Hospital.objects.get(user=self.request.user)
        queryset = Datashare.objects.filter(hospital=data)  
        return  queryset

#ambu
class updateuserAmbulancedatashare(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAuthenticated]
    authentication_classes = [TokenAuthentication] 
    queryset = AmbulnceDatashare.objects.all()
    serializer_class =PatientAmbDatashareSerializer

class getuserAmbulancedatashare(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    authentication_classes = [TokenAuthentication] 
    serializer_class = PatientAmbDatashareSerializer
    def get_queryset(self):
        queryset = AmbulnceDatashare.objects.filter(user=self.request.user)
        return  queryset

class getAmbulancedatashare(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    authentication_classes = [TokenAuthentication] 
    serializer_class = AmbulanceDatashareSerializer
    def get_queryset(self):
        data = Ambulance.objects.get(user=self.request.user)
        print(data)
        queryset = AmbulnceDatashare.objects.filter(Ambulance=data) 
        return  queryset


#doctor
class getuserdocdatashare(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    authentication_classes = [TokenAuthentication] 
    serializer_class = PatientdocDatashareSerializer
    def get_queryset(self):
        queryset = DocDatashare.objects.filter(user=self.request.user)
        return  queryset
        
class updateuserdocdatashar(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAuthenticated]
    authentication_classes = [TokenAuthentication] 
    queryset = DocDatashare.objects.all()
    serializer_class =updocDatashareSerializer

class getdocdatashare(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    authentication_classes = [TokenAuthentication] 
    serializer_class = DocDatashareSerializer
    def get_queryset(self):
        data = Doctor.objects.get(user=self.request.user) 
        queryset = DocDatashare.objects.filter(Doctor=data) 
        return  queryset

#Pathology
class getuser_pathdatashare(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    authentication_classes = [TokenAuthentication] 
    serializer_class = PatientpathologyDatashareSerializer
    def get_queryset(self):
        queryset = PathologyDatashare.objects.filter(user=self.request.user)
        return  queryset
        
class updateuser_pathdatashare(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAuthenticated]
    authentication_classes = [TokenAuthentication] 
    queryset = PathologyDatashare.objects.all()
    serializer_class =uppathDatashareSerializer

class getpath_datashare(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    authentication_classes = [TokenAuthentication] 
    serializer_class = pathDatashareSerializer
    def get_queryset(self):
        data = Pathologist.objects.get(user=self.request.user) 
        queryset = PathologyDatashare.objects.filter(pathologist=data) 
        return  queryset








        
#global data

class PharmaList(generics.ListCreateAPIView): 
    serializer_class = PharmaSerializer
    queryset = Pharmacist.objects.all()

class pharmaDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes=[IsAuthenticated]
    queryset = Pharmacist.objects.all()
    serializer_class = PharmaSerializer

class MedtList(generics.ListCreateAPIView): 
    serializer_class = MedSerializer
   
class MedDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventory.objects.all()
    serializer_class = MedSerializer


class doctorList(generics.ListCreateAPIView):
    # permission_classes=[IsAuthenticated]
    queryset = Doctor.objects.all()
    serializer_class = docotorSerializer
class doctorDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes=[IsAuthenticated]
    queryset = Doctor.objects.all()
    serializer_class = docotorSerializer

class PathologistList(generics.ListCreateAPIView):
    # permission_classes=[IsAuthenticated]
    queryset = Pathologist.objects.all()
    serializer_class = pathologistSerializer
class PathologistDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes=[IsAuthenticated]
    queryset = Pathologist.objects.all()
    serializer_class = pathologistSerializer

class hospList(generics.ListCreateAPIView):
    # permission_classes=[IsAuthenticated]
    queryset = Hospital.objects.all()
    serializer_class = hospitalSerializer

class hospDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes=[IsAuthenticated]
    queryset = Hospital.objects.all()
    serializer_class = hospitalSerializer


class Ambulancelist(generics.ListCreateAPIView):
    # permission_classes=[IsAuthenticated]
    queryset =Ambulance.objects.all()
    serializer_class = AmbulanceSerializer

class Ambulancedetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes=[IsAuthenticated]
    queryset = Ambulance.objects.all()
    serializer_class = AmbulanceSerializer


from django.http import HttpResponse, JsonResponse
@api_view(['GET'])
def GetPharmaMed(request,pk):
    product = Pharmacist.objects.get(id=pk)
    queryset=Inventory.objects.filter(Pharmacist=product)
    serializer = MedSerializer(queryset, many=True)
    return JsonResponse(serializer.data, safe=False)



#cart
class Userorder(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = Orderserializer
    def get_queryset(self):
        queryset= Order.objects.filter(user=self.request.user)
        return  queryset
   

class Usercart(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = Orderitemserializer
    def get_queryset(self):
        data = Order.objects.get(user=self.request.user,isPaid=False)
        print(data)
        queryset = Orderitem.objects.filter(order=data)  
        return  queryset



class GETUsercart(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = GETOrderitemserializer
    def get_queryset(self):
        data = Order.objects.get(user=self.request.user,isPaid=False)
        print(data)
        queryset = Orderitem.objects.filter(order=data)  
        return  queryset



class Usercartdetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orderitem.objects.all()
    serializer_class = Orderitemserializer

class Usershipping(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = ShippingAddressserializer
    def get_queryset(self):
        data= Order.objects.get(user=self.request.user,isPaid=False) 
        queryset = ShippingAddress.objects.filter(order=data)  
        return  queryset




@api_view(['GET', 'PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def cart(request,pro=None,q=1,pk=0):
    if request.method == 'GET':
        # GET CART ITEMS
        getch=Pharmacist.objects.get(id=pk) 
        print(getch)
        if Order.objects.filter(user=request.user,Pharmacist=getch,active=True).exists():
            order=Order.objects.get(user=request.user,Pharmacist=getch,active=True)
            carts = Orderitem.objects.filter(order=order)
            cart = Orderitemserializer(carts, many=True, context={'request': request})
            return Response(cart.data)
        else:
            return Response({"message": "your cart is empty"})
    elif request.method == 'PUT':
        product = Inventory.objects.get(id=pro)
        print(product)
        # DECREASE QUANTITY
        if q == '0':
            cart = Orderitem.objects.get(product=product, user=request.user, active=True)
            cart.quantity -= 1  # type: ignore
            cart.save()
        # ADD TO CART
        elif q == '2':
            vh=Pharmacist.objects.get(id=pk)
           # order=Order.objects.get(user=request.user,Pharmacist=vh,active=True)
            if Order.objects.filter(user=request.user,Pharmacist=vh,active=True).exists():
               order=Order.objects.get(user=request.user,Pharmacist=vh,active=True)
               if  Orderitem.objects.filter(product=product, user=request.user,order=order, active=True).exists():
                   return Response({"error": True, "message": "Already Added"})
               else:
                  vh=Pharmacist.objects.get(id=pk)
                  orderc=Order.objects.get(user=request.user,Pharmacist=vh,active=True)
                  order_item = Orderitem.objects.create(
                            product=product,
                            order=orderc,
                            user=request.user
                    )
                  order_item.save()
                  return Response({"message":"product is added"})
            else: 
                ordered_date = timezone.now()  # type: ignore
                ph=Pharmacist.objects.get(id=pk)
                print(ph)
                order = Order.objects.create(user=request.user,Pharmacist=ph,date_ordered=ordered_date)
                order.save()
                order_item = Orderitem.objects.create(   
                    product=product,
                    order=order,
                    user=request.user
                           )
                order_item.save()
                
        # INCREASE QUANTITY
        elif q == '1':
            cart = Orderitem.objects.get(product=product, user=request.user, active=True)
            cart.quantity += 1  # type: ignore
            cart.save()
        elif q == '3':
            ph=Pharmacist.objects.get(id=pk)
            ordera=Order.objects.get(user=request.user,Pharmacist=ph,active=True)
            cart = Orderitem.objects.get(product=product, user=request.user,order=ordera)
            cart.delete()
        # IF ERROR
        else:
            return Response({"error": True, "message": "Something went Wrong"})
    else:
        return Response({"error": True, "message": "Something went Wrong"})
    return Response({"error": False, "message": "Successfully Done"})















#pharma side
class pharmaorder(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = PhramaorderSerializer
    def get_queryset(self):
        data = Pharmacist.objects.get(user=self.request.user)
        queryset= Order.objects.filter(Pharmacist=data, isPaid =True, complete=False)  
        return  queryset

@api_view(['GET'])
def Getoderdetail(request,pk):
    product = Order.objects.get(id=pk)
    queryset=Orderitem.objects.filter(order=product)
    serializer = Orderitemserializer(queryset, many=True)
    return JsonResponse(serializer.data, safe=False)
 

@api_view(['GET'])
def Getodershiping(request,pk):
    product = Order.objects.get(id=pk)
    queryset=ShippingAddress.objects.filter(order=product)
    serializer = ShippingAddressserializer(queryset, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def GetPharmaMedser(request,pk,pro):
    product = Pharmacist.objects.get(id=pk)
    queryset=Inventory.objects.filter(Pharmacist=product,medicinename=pro)
    serializer = MedSerializer(queryset, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def marksascomplete(request,pk):
    Order.objects.filter(id=pk).update(complete=True)    
    return Response({"message":"order marked as complete"})

@api_view(['POST'])
def start_paymentOrder(request,pk):
    #  Order.objects.filter(id=pk).update(order_payment_id =payment['id'])
     value=request.data["value"]
     if value=="true":
       Order.objects.filter(id=pk).update(active=False,isPaid = True)
       return Response({"message":"order is paid"})
     else:
        return Response({"message":"payment failed"})



































# @api_view(['POST'])
# def start_paymentOrder(request,pk):
#     # request.data is coming from frontend
#     amount = request.data['amount']
#     # setup razorpay client this is the client to whome user is paying money that's you
#     client = razorpay.Client(auth=("rzp_test_8SYblYb1SY5Ixj", "s3ekF1bZRISt5IXjXNR6RtJi"))

#     # create razorpay order
#     # the amount will come in 'paise' that means if we pass 50 amount will become
#     # 0.5 rupees that means 50 paise so we have to convert it in rupees. So, we will 
#     # mumtiply it by 100 so it will be 50 rupees.
#     payment = client.order.create({"amount": int(amount) * 100, 
#                                    "currency": "INR", 
#                                    "payment_capture": "1"})

#     # we are saving an order with isPaid=False because we've just initialized the order
#     # we haven't received the money we will handle the payment succes in next 
#     # function
#     Order.objects.filter(id=pk).update(order_payment_id =payment['id'])
#     Order.objects.filter(id=pk).update(active=False)

#     # print(order)
#     # order.order_payment_id =payment['id']
#     # print( order.order_payment_id )
#     # order.save()

   

#     """order response will be 
#     {'id': 17, 
#     'order_date': '23 January 2021 03:28 PM', 
#     'order_product': '**product name from frontend**', 
#     'order_amount': '**product amount from frontend**', 
#     'order_payment_id': 'order_G3NhfSWWh5UfjQ', # it will be unique everytime
#     'isPaid': False}"""

#     data = {
#         "payment": payment,
#     }
#     return Response(data)


# @api_view(['POST'])
# def handle_payment_successorder(request):
#     # request.data is coming from frontend
#     res = json.loads(request.data["response"])

#     """res will be:
#     {'razorpay_payment_id': 'pay_G3NivgSZLx7I9e', 
#     'razorpay_order_id': 'order_G3NhfSWWh5UfjQ', 
#     'razorpay_signature': '76b2accbefde6cd2392b5fbf098ebcbd4cb4ef8b78d62aa5cce553b2014993c0'}
#     this will come from frontend which we will use to validate and confirm the payment
#     """

#     ord_id = ""
#     raz_pay_id = ""
#     raz_signature = ""

#     # res.keys() will give us list of keys in res
#     for key in res.keys():
#         if key == 'razorpay_order_id':
#             ord_id = res[key]
#         elif key == 'razorpay_payment_id':
#             raz_pay_id = res[key]
#         elif key == 'razorpay_signature':
#             raz_signature = res[key]

#     # get order by payment_id which we've created earlier with isPaid=False
#     order = Order.objects.get(order_payment_id=ord_id)

#     # we will pass this whole data in razorpay client to verify the payment
#     data = {
#         'razorpay_order_id': ord_id,
#         'razorpay_payment_id': raz_pay_id,
#         'razorpay_signature': raz_signature
#     }

#     client = razorpay.Client(auth=("rzp_test_8SYblYb1SY5Ixj", "s3ekF1bZRISt5IXjXNR6RtJi"))

#     # checking if the transaction is valid or not by passing above data dictionary in 
#     # razorpay client if it is "valid" then check will return None
#     check = client.utility.verify_payment_signature(data)

#     if check is not None:
#         print("Redirect to error url or error page")
#         return Response({'error': 'Something went wrong'})

#     # if payment is successful that means check is None then we will turn isPaid=True
#     Order.objects.filter(order_payment_id=ord_id).update(isPaid = True,active=False)  
#     # order.isPaid = True
#     # order.save()

#     res_data = {
#         'message': 'payment successfully received!'
#     }

#     return Response(res_data)


