from django import forms 
from django.forms import ModelForm
from . models import Employer_Profile, Job_Post, EmployerTerm, EmployerTerms2,EmployerPayment,EmployerPayment
from home.models import Category



class EmployerTermForm(forms.ModelForm):
    class Meta:
        model = EmployerTerm
        fields = "__all__"
     

class EmployerTerms2Form(forms.ModelForm):
    class Meta:
        model = EmployerTerms2
        fields = "__all__"
     
     

class EmployerCreateProfileForm(forms.ModelForm):
    class Meta:
        model = Employer_Profile
        fields = "__all__"
        
       

class Employer_ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Employer_Profile
        fields = ['company_name', 'address', 'city', 'state', 'phone',  'website', 'employer_logo', 'about_us']
        
       

class JobPostForm(forms.ModelForm):
    class Meta:
        model = Job_Post
        fields = "__all__"
     

class JobPostUpdateForm(forms.ModelForm):
    class Meta:
        model = Job_Post
        fields = ['category','job', 'slug', 'role', 'requirement', 'probabtion', 'location', 'additional_skills', 'employer_terms', 'job_description']
     


class EmployerPaymentForm(forms.ModelForm):
    class Meta:
        model = EmployerPayment
        fields = ['first_name','last_name','total','employer_number','pay_code','phone_no','paid','complete']
     