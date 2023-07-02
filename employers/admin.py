from django.contrib import admin

from . models import *
# Register your models here.

@admin.register(EmployerTerm)
class EmployerTermAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'paragraph1','paragraph2', 'paragraph3','paragraph4', 'paragraph5', 'paragraph6', 'paragraph7', 'terms1_date','agree1', 'complete']

    # def has_add_permission(self, request, obj=None):
    #     return False
    
    # def has_change_permission(self, request, obj=None):
    #     return False

    # def has_delete_permission(self, request, obj=None):
    #     return False


@admin.register(EmployerTerms2)
class EmployerTerms2Admin(admin.ModelAdmin):
    list_display = ['id', 'user', 'first_name','last_name','home_address','home_address','phone_no','terms2_date','attest','attest_paragraph','agree2','complete']

    # def has_add_permission(self, request, obj=None):
    #     return False
    
    # def has_change_permission(self, request, obj=None):
    #     return False

    # def has_delete_permission(self, request, obj=None):
    #     return False


@admin.register(Employer_Profile)
class Employer_profileAdmin(admin.ModelAdmin):
    list_display = ['user', 'company_name','slug', 'address', 'city', 'state', 'phone', 'website', 'employer_logo', 'about_us','complete']
    prepopulated_fields = {'slug': ('company_name',)}
    
    # def has_add_permission(self, request, obj=None):
    #     return False
    
    # def has_change_permission(self, request, obj=None):
    #     return False

    # def has_delete_permission(self, request, obj=None):
    #     return False


@admin.register(Job_Post)
class Job_PostAdmin(admin.ModelAdmin):
    list_display = ['id','employer_profile','employer_name','employ_logo','category','job','slug', 'role','publish', 'job_open','requirement', 'probabtion', 'location', 'additional_skills', 'job_updated', 'deadline','job_open_date','job_closed','job_closed_date','publish_date']
    list_display_links = ('id','employer_profile', 'job','role')
    # readonly_fields= ('image_tag',)
    prepopulated_fields = {'slug': ('num_alpha',)}
    list_per_page = 6

    # def has_add_permission(self, request, obj=None):
    #     return False
    
    # def has_change_permission(self, request, obj=None):
    #     return False

    # def has_delete_permission(self, request, obj=None):
    #     return False

    
@admin.register(EmployerPayment)
class EmployerPaymentAdmin(admin.ModelAdmin):
    list_display = ['id','user','first_name','last_name','total','employer_number','pay_code','phone_no','paid','complete']
    list_display_links = ('id','employer_number')
    # readonly_fields= ('user','total','employer_number','pay_code','phone_no','paid','complete')
    
    # def has_add_permission(self, request, obj=None):
    #     return False
    
    # def has_change_permission(self, request, obj=None):
    #     return False

    # def has_delete_permission(self, request, obj=None):
    #     return False



