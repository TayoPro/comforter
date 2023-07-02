from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import View


# email message setting 
from django.core.mail import EmailMessage
from django.conf import settings
# email message setting done

User = settings.AUTH_USER_MODEL

# password reset modules 
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import PasswordResetForm
from accounts.models import CustomUser
# from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
# password reset modules done

from applicants.models import General_Information,Job_Prospect,Health_History, Guarantor_Form,Guarantor_Form2,Terms_Conditions
from employers.models import Employer_Profile,EmployerTerm,EmployerTerms2,EmployerPayment
from home.models import CompanyProfile
from createdby.models import CreatedBy
from applicants.models import General_Information
from accounts.forms import ApplicantSignupForm, EmployerSignupForm, PasswordForm, RestPasswordForm
# Create your views here.

class AppliList(View):
    def get(self, request):
        return HttpResponse('accounts done')


class ApplicantList(View):
    def get(self, request):
        home = CompanyProfile.objects.get(pk=1)
        createdby = CreatedBy.objects.get(pk=1)
        return render(request, 'applicant_signin.html',{'home':home, 'createdby':createdby})

class EmployerList(View):
    def get(self, request):
        home = CompanyProfile.objects.get(pk=1)
        createdby = CreatedBy.objects.get(pk=1)
        return render(request, 'employer_signin.html', {'home':home, 'createdby':createdby})

# authentication system
class SignoutList(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'Signout successful')
        return redirect('accounts:applicantsignin')


class EmSignoutList(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'Signout successful')
        return redirect('accounts:employersignin')


class ApplicantSignin(View):
    def get(self, request):
        home = CompanyProfile.objects.get(pk=1)
        createdby = CreatedBy.objects.get(pk=1)
        return render(request, 'applicant_signin.html', {
            'home':home,
            'createdby':createdby
        })
    

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password1']
        user = authenticate(email = email, password = password)
        if user:
            if user.is_applicant == True:
                login(request, user)
                try:
                    genf = General_Information.objects.get(user = request.user, complete = True)
                    try:
                        jobp = Job_Prospect.objects.get(user_id= request.user.id)
                        try:
                            healh = Health_History.objects.get(user= request.user, complete = True)
                            try:
                                guarf = Guarantor_Form.objects.get(user= request.user, complete = True)
                                try:
                                    gauf2 = Guarantor_Form2.objects.get(user= request.user, complete = True)
                                    try:
                                        termc = Terms_Conditions.objects.get(user= request.user, complete = True)
                                        profile = General_Information.objects.get(user = request.user)
                                        fname = profile.first_name.title()
                                        messages.success(request, f'Hi {fname}, welcome to your dashboard!')
                                        return redirect('applicants:applicant_dashboard')
                                    except Terms_Conditions.DoesNotExist:
                                        return redirect('applicants:create_profile6')
                                except General_Information.DoesNotExist:
                                    return redirect('applicants:create_profile5')
                            except General_Information.DoesNotExist:
                                return redirect('applicants:create_profile4')
                        except Health_History.DoesNotExist:
                            return redirect('applicants:create_profile3')
                    except Job_Prospect.DoesNotExist:
                        return redirect('applicants:create_profile2') 
                except General_Information.DoesNotExist:
                    return redirect('applicants:create_profile1')
            else:
                messages.success(request, 'Restricted! Applicants Only.')
                return redirect('accounts:applicantsignin')
        else:
            messages.warning(request, 'Username/password incorrect')
            return redirect('accounts:applicantsignin')


class EmployerSignin(View):
    def get(self, request):
        home = CompanyProfile.objects.get(pk=1)
        createdby = CreatedBy.objects.get(pk=1)
        return render(request, 'employer_signin.html', {
            'home':home,
            'createdby':createdby
        })

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email = email, password = password)
        if user:
            if user.is_employer == True:
                login(request, user)
                try:
                    empt = EmployerTerm.objects.get(user= request.user, complete = True)
                    try:
                        empt2 = EmployerTerms2.objects.get(user= request.user, complete = True)
                        try:
                            empay = EmployerPayment.objects.filter(user= request.user, complete = True)   
                            try:
                                emp = Employer_Profile.objects.get(user= request.user, complete = True)
                                messages.success(request, 'Signin successful!')
                                return redirect('employers:employer_dashboard') 
                            except Employer_Profile.DoesNotExist:
                                messages.success(request, 'You have to create company profile')
                                return redirect('employers:create_profile')                       
                        except EmployerPayment.DoesNotExist:
                            messages.success(request, 'You are required to subscribe for Employer membership')
                            return redirect('employers:employer_pay')
                    except EmployerTerms2.DoesNotExist:
                        messages.warning(request, 'You are required to fill the client obligation form')
                        return redirect('employers:employer_term2')
                except EmployerTerm.DoesNotExist:
                    messages.warning(request, 'You are required to fill the agreement form')
                    return redirect('employers:employer_term')                 
            else:
                messages.success(request, 'Restricted! Employers Only.')
                return redirect('accounts:employersignin')
        else:
            messages.warning(request, 'Username/password is incorrect')
            return redirect('accounts:employersignin')


class ApplicantSignup(View):
    def get(self, request):
        home = CompanyProfile.objects.get(pk=1)
        createdby = CreatedBy.objects.get(pk=1)
        regform = ApplicantSignupForm()
        return render(request, 'applicant_signup.html', {
            'regform':regform,
            'home':home,
            'createdby':createdby
            })

    def post(self, request):
        regform = ApplicantSignupForm(request.POST)
        if regform.is_valid():
            reg = regform.save(commit = False)
            reg.is_applicant = True
            reg.save()
            login(request, reg)
            messages.success(request, 'Signup successful!')
            return redirect('applicants:create_profile1')
        else: 
            messages.error(request, regform.errors)
            return redirect('accounts:applicantsignup')


class EmployerSignup(View):
    def get(self, request):
        home = CompanyProfile.objects.get(pk=1)
        createdby = CreatedBy.objects.get(pk=1)
        regform = EmployerSignupForm()
        return render(request, 'employer_signup.html', {
            'regform':regform,
            'home':home,
            'createdby':createdby
            })

    def post(self, request):
        regform = EmployerSignupForm(request.POST)
        if regform.is_valid():
            reg = regform.save(commit=False)
            reg.is_employer = True
            newreg = reg.save()
            login(request, reg)
            messages.success(request, 'Signup successful!')
            return redirect('employers:employer_term')
        else:
            messages.error(request, regform.errors)
            return redirect('accounts:employersignup')

# #authentication system done 


# password reset 
class PasswordResetRequest(View):
    def get(self, request):
	    reset_form = PasswordResetForm()
	    return render(request=request, template_name="password/password_reset.html", context={"reset_form":reset_form})


    def post(self, request):
	    reset_form = PasswordResetForm(request.POST)
	    if reset_form.is_valid():
                data = reset_form.cleaned_data['email']
                users = CustomUser.objects.filter(Q(email=data))
                if users.exists():
                    for user in users:
                        subject = "Password Reset Requested"
                        email_template_name = "password/password_reset_email.txt"
                        change = {
                        "email":user,
                        # "email":user.email,
                        'domain':'127.0.0.1:8000',
                        'site_name': 'Comforter S.C Limited',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "email": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                        }
                        email = render_to_string(email_template_name, change)
                        try:
                            send_mail(subject, email, settings.EMAIL_HOST_USER, [user], fail_silently=False)
                        except BadHeaderError:
                            return HttpResponse('Invalid header found.')
                        return redirect ('password_reset/done')

	

