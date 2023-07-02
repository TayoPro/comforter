from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, PasswordResetForm
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import get_user_model
from django import forms 


class ComforterRegForm(UserCreationForm):
    email = forms.EmailField(max_length=150, widget= forms.EmailInput(attrs={'class': 'reg_input', 'placeholder': 'Enter email address'}))
    password1 = forms.CharField(max_length=150, widget= forms.PasswordInput(attrs={'class': 'reg_input', 'placeholder': 'Enter Old Password'}))
    password2 = forms.CharField(max_length=150, widget= forms.PasswordInput(attrs={'class': 'reg_input', 'placeholder': 'Enter Old Password'}))

    class Meta:
        model = get_user_model()
        fields = ('email', 'password1', 'password2')


class ApplicantSignupForm(UserCreationForm):
    email = forms.EmailField(max_length=150, widget= forms.EmailInput(attrs={'class': 'reg_input', 'placeholder': 'Enter email address'}))
    password1 = forms.CharField(max_length=150, widget= forms.PasswordInput(attrs={'class': 'reg_input', 'placeholder': 'Enter Old Password'}))
    password2 = forms.CharField(max_length=150, widget= forms.PasswordInput(attrs={'class': 'reg_input', 'placeholder': 'Enter Old Password'}))

    class Meta:
        model = get_user_model()
        fields = ('email', 'password1', 'password2')

""" 
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email']

    def clean_email(self):
        '''
        Verify email is available.
        '''
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email

    def clean(self):
        '''
        Verify both passwords match.
        '''
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password")
        password2 = cleaned_data.get("password_2")
        if password is not None and password1 != password2:
            self.add_error("password2", "Your passwords must match")
        return cleaned_data

"""
 

class EmployerSignupForm(UserCreationForm):
    # company_name = forms.CharField(max_length=250, widget= forms.TextInput(attrs={'class': 'reg_input', 'placeholder': 'Enter email address'}))
    email = forms.EmailField(max_length=150, widget= forms.EmailInput(attrs={'class': 'reg_input', 'placeholder': 'Enter email address'}))
    password1 = forms.CharField(max_length=150, widget= forms.PasswordInput(attrs={'class': 'reg_input', 'placeholder': 'Enter Old Password'}))
    password2 = forms.CharField(max_length=150, widget= forms.PasswordInput(attrs={'class': 'reg_input', 'placeholder': 'Enter Old Password'}))
      

    class Meta:
        model = get_user_model()
        fields = ('email', 'password1', 'password2')


class PasswordForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=50, widget= forms.PasswordInput(attrs={'class': 'passinput', 'placeholder': 'Enter Old Password'}))
    new_password1 = forms.CharField(max_length=50, widget= forms.PasswordInput(attrs={'class': 'passinput', 'placeholder': 'Enter New Password'}))
    new_password2 = forms.CharField(max_length=50, widget= forms.PasswordInput(attrs={'class': 'passinput', 'placeholder': 'Repeat New Password'}))

    class Meta:
        model = get_user_model()
        fields = ('old_password', 'new_password1', 'new_password2')

    def __init__(self,*args, **kwargs):
        super(PasswordForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs['class'] = 'passinput'
        self.fields['new_password1'].widget.attrs['class'] = 'passinput'
        self.fields['new_password2'].widget.attrs['class'] = 'passinput'


class RestPasswordForm(PasswordResetForm):
    email = forms.EmailField(max_length=50, widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter your email address.'}))
    
    class Meta:
        model = get_user_model() 
        fields = ('email',)


    def __init__(self,*args, **kwargs):
        super(RestPasswordForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['class'] = 'form-control'


