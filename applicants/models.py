from django.db import models
from django.contrib.auth import get_user_model  
# User = get_user_model()
# from PIL import Image
from django.urls import reverse
from django.conf import settings
# from django.utils import timezone

User = settings.AUTH_USER_MODEL


from employers.models import Job_Post, Employer_Profile
# Create your models here.


class General_Information(models.Model):#createprofile
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=250)
    mobile_number = models.CharField(max_length=11)
    home_number = models.CharField(max_length=11)
    current_address = models.CharField(max_length=250)
    nearest_bus_stop = models.CharField(max_length=250)
    landmark = models.CharField(max_length=250)
    current_city = models.CharField(max_length=250)
    current_state = models.CharField(max_length=250)
    qualification = models.CharField(max_length=250)
    date_of_birth = models.CharField(max_length=250)
    gender = models.CharField(max_length=250)    
    image = models.ImageField(upload_to='profile', default='profile/avatar.jpg') 
    state_of_origin = models.CharField(max_length=250)    
    local_gov_area = models.CharField(max_length=250)    
    parents_address = models.CharField(max_length=250)    
    parents_phone_number = models.CharField(max_length=250)    
    name_of_your_village = models.CharField(max_length=250)    
    family_compound_name  = models.CharField(max_length=250)    
    marital_status = models.CharField(max_length=250)
    complete = models.BooleanField(default = False)


    def __str__(self):
        return self.user.email
               
    class Meta:
        db_table = 'general_information'
        managed = True
        verbose_name = 'General_Information'
        verbose_name_plural = 'General_Information'




class Job_Prospect(models.Model):#CreateProfile2
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    post_applied_for = models.CharField(max_length=250)
    years_of_experience = models.IntegerField()
    expected_salary = models.CharField(max_length=250, default='')
    intended_time_to_work = models.CharField(max_length=250)
    ever_convicted = models.CharField(max_length=5)
    your_off_days = models.CharField(max_length=150)
    travel_period = models.CharField(max_length=250)
    travel_period_reason = models.CharField(max_length=250)
    how_did_you_know_us = models.CharField(max_length=250)
    name_phone = models.CharField(max_length=250, blank=True, null=True)
    application_date = models.DateTimeField(auto_now_add=True)
    employer_address = models.CharField(max_length=250, blank=True, null=True)
    employe_name = models.CharField(max_length=250, blank=True, null=True)
    company_name = models.CharField(max_length=250, blank=True, null=True)
    employer_phone = models.CharField(max_length=11, blank=True, null=True)
    work_type = models.CharField(max_length=50, blank=True, null=True)
    resign_reason = models.CharField(max_length=250, blank=True, null=True)
    register_with_agent = models.CharField(max_length=250)
    agent_phone = models.CharField(max_length=11, blank=True, null=True)
    agent_address = models.CharField(max_length=250, blank=True, null=True)
    complete = models.BooleanField(default = False)


    def __str__(self):
        return self.user.email

    class Meta:
        db_table = 'job_prospect'
        managed = True
        verbose_name = 'Job_Prospect'
        verbose_name_plural = 'Job_Prospect'



class Health_History(models.Model):#CreateProfile3
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    disability = models.CharField(max_length=50, blank=True, null=True)
    state_disability = models.CharField(max_length=250, blank=True, null=True)
    use_glasses = models.CharField(max_length=50)
    do_you_smoke = models.CharField(max_length=50)
    take_alcohol = models.CharField(max_length=50)
    on_medication = models.CharField(max_length=50, blank=True, null=True)
    medicine_name = models.CharField(max_length=250, blank=True, null=True)
    blood_group = models.CharField(max_length=50)
    genotype = models.CharField(max_length=50)
    school_attended = models.CharField(max_length=250)
    can_you_read = models.CharField(max_length=50)
    can_you_write = models.CharField(max_length=50)
    speak_fluently = models.CharField(max_length=50)
    language_spoken = models.CharField(max_length=250, blank=True, null=True)
    spouse_name = models.CharField(max_length=250)
    no_children = models.IntegerField()
    spouse_address = models.CharField(max_length=250)
    spouse_bstop = models.CharField(max_length=250)
    spouse_phone = models.CharField(max_length=12)
    family_name = models.CharField(max_length=250)
    family_address = models.CharField(max_length=250, default='')
    family_occupation = models.CharField(max_length=250)
    family_phone = models.CharField(max_length=250)
    reference_name = models.CharField(max_length=250)
    reference_address = models.CharField(max_length=250)
    reference_occupation = models.CharField(max_length=250)
    reference_number = models.CharField(max_length=250)
    attest = models.TextField()
    complete = models.BooleanField(default = False)


    def __str__(self):
        return self.user.email

    class Meta:
        db_table = 'health_history'
        managed = True
        verbose_name = 'Health_History'
        verbose_name_plural = 'Health_History'



class Guarantor_Form(models.Model):#createprofile4
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    gimage = models.ImageField(upload_to='guarantor', default='guarantor/avatar.jpg') 
    guarantor_name = models.CharField(max_length=250)
    guarantor_address = models.CharField(max_length=250)
    guarantor_phone = models.CharField(max_length=12)
    guarantor_company = models.CharField(max_length=250)    
    guarantor_address = models.CharField(max_length=250)    
    guarantor_position = models.CharField(max_length=250)    
    guarantor_office_phone = models.CharField(max_length=12)
    guarantor_origin = models.CharField(max_length=250) 
    guarantor_lga = models.CharField(max_length=250) 
    guarantor_name_phone = models.CharField(max_length=250) 
    guarantor_spouse_address = models.CharField(max_length=250) 
    how_do_you_know_him = models.CharField(max_length=250) 
    attest = models.TextField() 
    applicant_name = models.CharField(max_length=250) 
    well_known_to_you = models.CharField(max_length=250) 
    relationship_with = models.CharField(max_length=250) 
    know_for_how_long = models.CharField(max_length=250) 
    attestation_date = models.DateTimeField(auto_now_add= True)
    agree = models.BooleanField()
    complete = models.BooleanField(default = False)


    def __str__(self):
        return self.user.email

    class Meta:
        db_table = 'guarantor_form'
        managed = True
        verbose_name = 'Guarantor_Form'
        verbose_name_plural = 'Guarantor_Forms'



class Guarantor_Form2(models.Model):#createprofile5
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    g2image = models.ImageField(upload_to='guarantor', default='guarantor/avatar.jpg') 
    guarantor_name = models.CharField(max_length=250)
    guarantor_address = models.CharField(max_length=250)
    guarantor_position = models.CharField(max_length=250)    
    guarantor_phone = models.CharField(max_length=12)      
    guarantor_origin = models.CharField(max_length=250) 
    guarantor_lga = models.CharField(max_length=250) 
    guarantor_relative_address = models.CharField(max_length=250) 
    applicant_name = models.CharField(max_length=250) 
    relationship = models.CharField(max_length=250, default='') 
    dated_this_day = models.DateTimeField(auto_now=True) 
    date_filled = models.DateTimeField(auto_now = True)
    witnes_name = models.CharField(max_length=250) 
    witnes_address = models.CharField(max_length=250) 
    witnes_phone = models.CharField(max_length=12) 
    witnesed_date = models.DateTimeField(max_length=100) 
    witnes_agree = models.BooleanField()
    complete = models.BooleanField(default = False)


    def __str__(self):
        return self.user.email

    class Meta:
        db_table = 'guarantor_form2'
        managed = True
        verbose_name = 'Guarantor_Form2'
        verbose_name_plural = 'Guarantor_Forms2'




class Terms_Conditions(models.Model):#CreateProfile6
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    please_ensure = models.TextField(blank=True, null=True)
    our_mission = models.TextField(blank=True, null=True)
    your_job = models.TextField(blank=True, null=True)
    attest = models.TextField()
    agree = models.BooleanField()
    complete = models.BooleanField(default = False)
    

    def __str__(self):
        return self.user.email

    class Meta:
        db_table = 'terms_conditions'
        managed = True
        verbose_name = 'Terms_Conditions'
        verbose_name_plural = 'Terms_Conditions'




class Job_Apply(models.Model):
    general_information = models.ForeignKey(General_Information,blank=True, null=True, on_delete=models.CASCADE)
    job_post = models.ForeignKey(Job_Post, blank=True, null=True, on_delete=models.CASCADE)
    empl_logo = models.ImageField(upload_to='employer_profile',  blank=True, null=True) 
    employer = models.CharField(max_length=250)
    category_apply = models.CharField(max_length=250, blank=True, null=True)
    job = models.CharField(max_length=250)
    slug = models.SlugField(blank=True, null=True, unique=True)
    role = models.CharField(max_length=250)
    requirement = models.CharField(max_length=250) 
    probabtion = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    additional_skills = models.CharField(max_length=250, blank=True, null=True) 
    previous_company = models.CharField(max_length=250, blank=True, null=True) 
    language_spoken = models.CharField(max_length=250, blank=True, null=True) 
    employer_terms = models.TextField(blank=True, null=True)
    job_description = models.TextField()
    salary_expected = models.CharField(max_length=50, blank=True, null=True)
    about_yourself = models.TextField()
    deadline_date = models.CharField(max_length=250, blank=True, null=True)
    job_date = models.DateTimeField(auto_now_add=True)
    job_dat = models.DateField(auto_now_add=True)
    job_updated = models.DateTimeField(auto_now_add=True)
    new_applied = models.BooleanField(blank=True, null=True)
    applied = models.BooleanField(blank=True, null=True) 
    applied_date = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    selected = models.BooleanField(default=False)
    shortlisted = models.BooleanField(default=False)
    shortlisted_date = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    declined = models.BooleanField(default=False)
    declined_date = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    hired = models.BooleanField(default=False)
    hireded_date = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    resigned = models.BooleanField(default=False)
    resigned_date = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    terminated = models.BooleanField(default=False)
    terminated_date = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    notice = models.IntegerField(default=1)
    admin_note = models.TextField(blank=True, null=True)
    
    
    def __str__(self):
        return self.general_information.user.email
    

    def get_absolute_url(self):
        return reverse("job_apply_detail", kwargs={"slug": self.slug})


    class Meta:
        db_table = 'job_apply'
        managed = True
        verbose_name = 'Job_Apply'
        verbose_name_plural = 'Job_Apply'
        

class ApplicantPayment(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    first_name= models.CharField(max_length = 150, blank=True, null=True)
    last_name= models.CharField(max_length = 150, blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    applicant_number = models.CharField(max_length=250, blank=True, null=True)
    pay_code = models.CharField(max_length=250, blank=True, null=True)
    phone_no = models.CharField(max_length=250, blank=True, null=True)
    paid = models.BooleanField(default = False)
    complete = models.BooleanField(default = False)

    def __str__(self):
        return self.user.email

    class Meta:
        db_table = 'applicantpayment'
        managed = True
        verbose_name = 'ApplicantPayment'
        verbose_name_plural = 'ApplicantPayments'
