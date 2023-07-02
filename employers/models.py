from django.db import models
from django.conf import settings
# from django.template.defaultfilters import slugify
from django.urls import reverse

User = settings.AUTH_USER_MODEL
# Create your models here.

from home.models import Category

# complete = models.BooleanField(default = False)
class Employer_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    company_name = models.CharField(max_length=250)
    slug = models.SlugField(blank=True, null=True,  unique=True)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    state = models.CharField(max_length=250)
    phone = models.CharField(max_length=20)
    website = models.URLField(default='', blank=True, null=True)
    employer_logo = models.ImageField(upload_to='employer_profile', default='employer_profile/company.png') 
    about_us = models.TextField()
    complete = models.BooleanField(default = False)


    def __str__(self):
        return self.user.email
    

    class Meta:
        db_table = 'profile'
        managed = True
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'




class Job_Post(models.Model):
    employer_profile = models.ForeignKey(Employer_Profile,blank=True, null=True, on_delete=models.CASCADE)
    employer_name = models.CharField(max_length=50, blank=True, null=True) 
    employ_logo = models.ImageField(upload_to='employer_profile',  blank=True, null=True) 
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE)
    job = models.CharField(max_length=250)
    num_alpha = models.CharField(max_length=250,  blank=True, null=True)
    slug = models.SlugField(blank=True, null=True,  unique=True)
    role = models.CharField(max_length=250)
    requirement = models.CharField(max_length=250)
    probabtion = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    additional_skills = models.CharField(max_length=250)
    employer_terms = models.TextField()
    job_description = models.TextField()
    publish = models.BooleanField(default=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    job_updated = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    deadline = models.CharField(max_length=250)
    job_open = models.BooleanField(default=True)
    job_open_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    job_closed = models.BooleanField(default=False)
    job_closed_date = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    

    def __str__(self):
        return self.employer_profile.user.email
    

    def get_absolute_url(self):
        return reverse("job_post_detail", kwargs={"slug": self.slug})

    
    class Meta:
        db_table = 'job_post'
        managed = True
        verbose_name = 'Job_Post'
        verbose_name_plural = 'Job_Posts'



class EmployerTerm(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    paragraph1 = models.CharField(max_length=250, blank=True, null=True)
    paragraph2 = models.CharField(max_length=250, blank=True, null=True)
    paragraph3 = models.CharField(max_length=250, blank=True, null=True)
    paragraph4 = models.CharField(max_length=250, blank=True, null=True)
    paragraph5 = models.CharField(max_length=250, blank=True, null=True)
    paragraph6 = models.CharField(max_length=250, blank=True, null=True)
    paragraph7 = models.CharField(max_length=250, blank=True, null=True)
    terms1_date = models.DateTimeField(auto_now_add=True)
    agree1 = models.BooleanField(default = False)
    complete = models.BooleanField(default = False)

    def __str__(self):
        return self.user.email

    class Meta:
        db_table = 'employerterm'
        managed = True
        verbose_name = 'EmployerTerm'
        verbose_name_plural = 'EmployerTerms'
        

class EmployerTerms2(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=250, blank=True, null=True)
    last_name = models.CharField(max_length=250, blank=True, null=True)
    home_address = models.CharField(max_length=250, blank=True, null=True)
    office_address = models.CharField(max_length=250, blank=True, null=True)
    phone_no = models.CharField(max_length=250, blank=True, null=True)
    terms2_date = models.DateTimeField(auto_now_add=True)
    attest = models.CharField(max_length=250, blank=True, null=True)
    attest_paragraph = models.CharField(max_length=250, blank=True, null=True)
    agree2 = models.BooleanField(default = False)
    complete = models.BooleanField(default = False)

    def __str__(self):
        return self.user.email

    class Meta:
        db_table = 'employerterms2'
        managed = True
        verbose_name = 'EmployerTerms2'
        verbose_name_plural = 'EmployerTerms2'



class EmployerPayment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    first_name= models.CharField(max_length = 150, blank=True, null=True)
    last_name= models.CharField(max_length = 150, blank=True, null=True)
    total = models.IntegerField()
    employer_number = models.CharField(max_length=250, blank=True, null=True)
    pay_code = models.CharField(max_length=250, blank=True, null=True)
    phone_no = models.CharField(max_length=250, blank=True, null=True)
    paid = models.BooleanField(default = False)
    complete = models.BooleanField(default = False)

    def __str__(self):
        return self.user.email

    class Meta:
        db_table = 'employerpayment'
        managed = True
        verbose_name = 'EmployerPayment'
        verbose_name_plural = 'EmployerPayments'
