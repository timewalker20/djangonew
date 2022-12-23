from django.urls import path
from . import views
from django.urls import path
from knox import views as knox_views
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api-token-auth/', views.CustomAuthToken.as_view()),
    path('register/',views.RegisterAPI.as_view()),
    path('verify/',views.verifyOTP.as_view()),
    path('Forget-Password/',views.ForgetPassword),
    path('Password-Reset/',views.PasswordReset),
    path('userdetails/',views.profilepack.as_view()),
    path('endcall/',views.endcall),
    #private...profile
    #path('User-Patientlist/', views.UserPatientList.as_view()),
    #path('Patient-list/<int:pk>/', views.UserPatientDetail.as_view()),

    #user pharma
    path('User-pharmalist/', views.UserPharmaList.as_view()),
    path('Userpharmalist/<int:pk>/', views.UserpharmaDetail.as_view()),
    path('User-medlist/', views.UserMedtList.as_view()),
    path('med-list/<int:pk>/', views.UserMedDetail.as_view()),

    #doctor
    path('User-doctorlist/', views.UserdoctorList.as_view()),
    path('User-doctorlist/<int:pk>/', views.UserdoctorDetail.as_view()),
   #pathology
    path('User-pathologistlist/', views.UserPathologistList.as_view()),
    path('User-pathologistdetails/<int:pk>/', views.UserPathologistList.as_view()),
    #hospital
    path('User-hosplist/', views.UserhospList.as_view()),
    path('hosp-list/<int:pk>/', views.UserhospDetail.as_view()),



    path('ambu-list/', views.UserAmbulancelist.as_view()),
    path('ambu-list/<int:pk>/', views.UserAmbulancelist.as_view()),
    # path('driver-list/', views.driverlist.as_view()),
    # path('driver-list/<int:pk>/', views.driverDetail.as_view()),
    #datashare
    #user side
    path('user-datashare/',views.getuserdatashare.as_view()),
    path('up-Hospdatashare/<int:pk>/',views.updategetuserdatashare.as_view()),
    #hospital side
    path('hosp-datashare/',views.gethospitaldatashare.as_view()),

    #user side
    path('user-Ambulancedatashare/',views.getuserAmbulancedatashare.as_view()),
    path('up-ambudatashare/<int:pk>/',views.updateuserAmbulancedatashare.as_view()),
    #hospital side
    path('ambu-Ambulancedatashare/',views.getAmbulancedatashare.as_view()),
    #doc
    path('user-docdatashare/',views.getuserdocdatashare.as_view()),
    path('up-docdatashare/<int:pk>/',views.updateuserdocdatashar.as_view()),
    path('doc-datashare/',views.getdocdatashare.as_view()),
    path('booking-pay/', views.start_payment, name="payment"),
    #path('payment/success/', views.handle_payment_success, name="payment_success"),
    path('paymenthandler',views.paymenthandler,),
    path('user-docbook/',views.getuserbooking.as_view()),
    path('doc-docbook/',views.getdocbooking.as_view()),
    #Pathology
    path('user-pathdatashare/',views.getuser_pathdatashare.as_view()),
    path('up-pathdatashare/<int:pk>/',views.updateuser_pathdatashare.as_view()),
    path('path-datashare/',views.getpath_datashare.as_view()),
    path('pathbooking-pay/', views.start_payment_Pathology, name="payment"),
    path('paymenthandler',views.paymenthandler,),
    path('user-pathbook/',views.getuser_pathbooking.as_view()),
    path('path-pathbook/',views.getpath_booking.as_view()),

    #global data
    path('all-pharmalist/', views.PharmaList.as_view()),
    path('all-pharmalist/<int:pk>/', views.UserpharmaDetail.as_view()),
    path('medlist/<int:pk>/', views.MedtList.as_view()),
    path('all-medlist/<int:pk>/', views.MedDetail.as_view()),
    path('all-hosplist/', views.hospList.as_view()),
    path('all-hosplist/<int:pk>/', views.hospDetail.as_view()),
    path('all-doctorlist/', views.doctorList.as_view()),
    path('all-doctorlist/<int:pk>/', views.doctorDetail.as_view()),
    path('all-ambulist/', views.Ambulancelist.as_view()),
    path('all-ambulist/<int:pk>/', views.Ambulancelist.as_view()),
    path('all-pathologylist/', views.PathologistList.as_view()),
    path('all-pathologylist/<int:pk>/', views.PathologistDetail.as_view()),
    path('pharmamed/<int:pk>/',views.GetPharmaMed,),#<str:poll_id>
    path('pharmamed/<int:pk>/<str:pro>',views.GetPharmaMedser,),
  #medicine buy
    path('user-order/', views.Userorder.as_view()),  
    path('postuser-cart/', views.Usercart.as_view()),
    path('getuser-cart/', views.GETUsercart.as_view()),
    path('cart-detail-delete/<int:pk>/',views.Usercartdetail.as_view()),
    path('usershipadd/', views.Usershipping.as_view()),

    path('cart/<pro>/<q>/<int:pk>',views.cart),
  
    path('order-pay/<int:pk>/', views.start_paymentOrder, name="payment"),
    #path('orderpayment/success/', views.handle_payment_successorder, name="payment_success"),
    path('orderlistpharma/', views.pharmaorder.as_view()),
    path('Getoderdetail/<int:pk>/',views.Getoderdetail),
    path(' Getodershiping/<int:pk>/',views.Getodershiping),
    path('mark-complete/',views.marksascomplete)
]

urlpatterns = format_suffix_patterns(urlpatterns)