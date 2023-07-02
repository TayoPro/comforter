from django.contrib import admin
# from django.apps import apps
from . models import *


# Register your models here.
@admin.register(General_Information)
class General_InformationAdmin(admin.ModelAdmin):
    list_display = ['user','first_name', 'middle_name', 'last_name', 'nationality', 'mobile_number', 'home_number', 'current_address', 'nearest_bus_stop', 'landmark','current_city', 'current_state','qualification','date_of_birth','gender','image','state_of_origin','local_gov_area','parents_address','parents_phone_number','name_of_your_village','family_compound_name','marital_status','complete']
    list_per_page = 5

    # def has_add_permission(self, request, obj=None):
    #     return False
    
    # def has_change_permission(self, request, obj=None):
    #     return False

    # def has_delete_permission(self, request, obj=None):
    #     return False

@admin.register(Job_Prospect)
class Job_ProspectAdmin(admin.ModelAdmin):
    list_display = ['id','user','post_applied_for','years_of_experience','intended_time_to_work','ever_convicted','your_off_days','travel_period','travel_period_reason','how_did_you_know_us','name_phone','application_date','employer_address','employe_name','company_name','employer_phone','work_type','resign_reason','register_with_agent','agent_phone','agent_address','complete']
    list_per_page = 5

    # def has_add_permission(self, request, obj=None):
    #     return False
    
    # def has_change_permission(self, request, obj=None):
    #     return False

    # def has_delete_permission(self, request, obj=None):
    #     return False


@admin.register(Health_History)
class Health_HistoryAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'language_spoken','spouse_name','no_children','spouse_address','spouse_bstop','spouse_phone','family_name','family_occupation','family_phone','reference_name','reference_address','reference_occupation','reference_number','attest','complete']
    list_per_page = 5

    # def has_add_permission(self, request, obj=None):
    #     return False
    
    # def has_change_permission(self, request, obj=None):
    #     return False

    # def has_delete_permission(self, request, obj=None):
    #     return False


@admin.register(Guarantor_Form)
class Guarantor_FormAdmin(admin.ModelAdmin):
    list_display = ['id','user','gimage','guarantor_name','guarantor_address', 'guarantor_address','guarantor_position','guarantor_office_phone','guarantor_origin','guarantor_lga','guarantor_name_phone','guarantor_spouse_address','how_do_you_know_him','attest','applicant_name','well_known_to_you','relationship_with','know_for_how_long', 'attestation_date','agree','complete']
    list_per_page = 5

    # def has_add_permission(self, request, obj=None):
    #     return False
    
    # def has_change_permission(self, request, obj=None):
    #     return False

    # def has_delete_permission(self, request, obj=None):
    #     return False


@admin.register(Guarantor_Form2)
class Guarantor_Form2Admin(admin.ModelAdmin):
    list_display = ['id', 'user','g2image','guarantor_name','guarantor_address','guarantor_position','guarantor_phone','guarantor_origin','guarantor_lga','guarantor_relative_address','applicant_name','relationship', 'dated_this_day','date_filled','witnes_name','witnes_address','witnes_phone','witnesed_date','witnes_agree','complete']
    list_per_page = 5

    # def has_add_permission(self, request, obj=None):
    #     return False
    
    # def has_change_permission(self, request, obj=None):
    #     return False

    # def has_delete_permission(self, request, obj=None):
    #     return False


@admin.register(Terms_Conditions)
class Terms_ConditionsAdmin(admin.ModelAdmin):
    list_display = ['id','user','please_ensure','our_mission','your_job','attest','agree','complete']
    list_per_page = 5

    # def has_add_permission(self, request, obj=None):
    #     return False
    
    # def has_change_permission(self, request, obj=None):
    #     return False

    # def has_delete_permission(self, request, obj=None):
    #     return False


@admin.register(Job_Apply)
class Job_ApplyAdmin(admin.ModelAdmin):
    list_display = ['id','general_information','job_post','empl_logo','employer','category_apply','job','slug', 'role','requirement', 'probabtion', 'location', 'additional_skills','previous_company','language_spoken', 'job_date','job_updated', 'deadline_date','salary_expected','about_yourself','hired','resigned','terminated','applied','shortlisted','declined','notice','applied_date','shortlisted_date','hireded_date','resigned_date','terminated_date','admin_note']
    list_display_links = ('id','general_information', 'job','role')
    readonly_fields=  ['id','general_information','job','slug', 'role','requirement', 'probabtion', 'location', 'additional_skills', 'job_date','job_updated', 'deadline_date','salary_expected','about_yourself']
    list_per_page = 5

    # def has_add_permission(self, request, obj=None):
    #     return False
    
    # def has_change_permission(self, request, obj=None):
    #     return False

    # def has_delete_permission(self, request, obj=None):
    #     return False


@admin.register(ApplicantPayment)
class ApplicantPaymentAdmin(admin.ModelAdmin):
    list_display = ['id','user','first_name','last_name','total','applicant_number','pay_code','phone_no','paid','complete']
    list_display_links = ('id','applicant_number')
    # readonly_fields= ('user','total','applicant_number','pay_code','phone_no','paid','complete')
    
    # def has_add_permission(self, request, obj=None):
    #     return False

    
    # def has_change_permission(self, request, obj=None):
    #     return False

    # def has_delete_permission(self, request, obj=None):
    #     return False



# applicants_models = apps.get_app_config('applicants').get_models()

# for model in applicants_models:
#     admin.site.register(model)

#use below when a model is already registered in the admin
# for model in post_models:
#     try:
#         admin.site.register(model)
#     except admin.sites.AlreadyRegistered:
#         pass