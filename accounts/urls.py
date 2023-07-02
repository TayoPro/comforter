from django.urls import path
from . views import *


app_name = 'accounts'

urlpatterns = [
    path('', AppliList.as_view(), name='appli'),
    path('applicant/', ApplicantList.as_view(), name='applicant'),
    path('employer', EmployerList.as_view(), name='employer'),
    path('signout', SignoutList.as_view(), name='signout'),
    path('employer/signout', EmSignoutList.as_view(), name='employer_signout'),
    path('applicant/signin', ApplicantSignin.as_view(), name='applicantsignin'),
    path('employer/signin', EmployerSignin.as_view(), name='employersignin'),
    path('applicant/signup', ApplicantSignup.as_view(), name='applicantsignup'),
    path('employer/signup', EmployerSignup.as_view(), name='employersignup'),
    path('password_reset', PasswordResetRequest.as_view(), name='password_reset'),
]
