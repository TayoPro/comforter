from django import forms
from django.forms import ModelForm
from . models import General_Information,Job_Prospect,Health_History, Guarantor_Form,Guarantor_Form2,Terms_Conditions,Job_Apply,ApplicantPayment

class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = General_Information
        fields = "__all__"
        
       

class CreateProfileForm2(forms.ModelForm):
    class Meta:
        model = Job_Prospect
        fields = "__all__"
       
      
        
class CreateProfileForm3(forms.ModelForm):
    class Meta:
        model = Health_History
        fields = "__all__"
      
        
class CreateProfileForm4(forms.ModelForm):
    class Meta:
        model = Guarantor_Form
        fields = "__all__"


      
class CreateProfileForm5(forms.ModelForm):
    class Meta:
        model = Guarantor_Form2
        fields = "__all__"


      
class CreateProfileForm6(forms.ModelForm):
    class Meta:
        model = Terms_Conditions
        fields = "__all__"

      
# update begins 
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = General_Information
        fields = ['first_name', 'middle_name', 'last_name', 'nationality', 'mobile_number', 'home_number', 'current_address', 'nearest_bus_stop', 'landmark','current_city', 'current_state','date_of_birth','gender','image','state_of_origin','local_gov_area','parents_address','parents_phone_number','name_of_your_village','family_compound_name','marital_status']


class ProfileUpdateForm2(forms.ModelForm):
    class Meta:
        model = Job_Prospect
        fields = "__all__"


class ProfileUpdateForm3(forms.ModelForm):
    class Meta:
        model = Health_History
        fields = "__all__"


class ProfileUpdateForm4(forms.ModelForm):
    class Meta:
        model = Guarantor_Form
        fields = "__all__"


class ProfileUpdateForm5(forms.ModelForm):
    class Meta:
        model = Guarantor_Form2
        fields = "__all__"



class JobApplyForm(forms.ModelForm):
    class Meta:
        model = Job_Apply
        fields = ['job', 'slug', 'role', 'requirement', 'probabtion', 'location', 'additional_skills', 'employer_terms', 'job_description', 'salary_expected','about_yourself']
     

class ApplicantPaymentForm(forms.ModelForm):
    class Meta:
        model = ApplicantPayment
        fields = ['first_name','last_name','total','applicant_number','pay_code','phone_no','paid','complete']
     