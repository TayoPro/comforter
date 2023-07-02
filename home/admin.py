from django.contrib import admin
from . models import CompanyProfile, Contact, Featured_Company, Registration_Fee, Category,Service
# Register your models here.

@admin.register(CompanyProfile)
class CompanyProfileAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'keyword', 'description', 'logo', 'banner','favicon', 'mobile1', 
    'mobile2','mobile3','mobile4','mobile5', 'head_office','branch_office1','branch_office2',
     'email', 'website','about', 'about2','about_img']
    list_display_links = ['id','name', 'keyword']
    
    def has_add_permission(self, request, obj=None):
        return False

    
    # def has_change_permission(self, request, obj=None):
    #     return False

    def has_delete_permission(self, request, obj=None):
        return False

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save_and_continue'] = False
        # extra_context['show_save'] = False
        return super(CompanyProfileAdmin, self).changeform_view(request, object_id, extra_context=extra_context)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category_name', 'cat_slug']
    prepopulated_fields = {'cat_slug': ('category_name',)}


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id','category','title','slug','job_image','job_description',
                    'list_title','list_item1','list_item2','list_item3','list_item4','list_item5','list_item6','list_item7','list_item8','list_item9','list_item10',
                    'list2_item1','list2_item2','list2_item3','list2_item4','list2_item5','list2_item6','list2_item7','list2_item8']
    prepopulated_fields = {'slug': ('title',)}
    list_display_links = ['id','category','title']
    list_per_page = 5


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name','email', 'phone', 'message', 'created', 'cleared', 'admin_note', 'status']
    list_per_page = 20
    readonly_fields = ['id', 'full_name','email']


@admin.register(Featured_Company)
class Featured_CompanyAdmin(admin.ModelAdmin):
    list_display = ['id', 'c_img']


@admin.register(Registration_Fee)
class Registration_FeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'currency_symbol', 'applicant_fee','worker_year_fee','employer_fee','large_company']
    list_display_links = ['currency_symbol', 'applicant_fee','worker_year_fee']
    

    def has_add_permission(self, request, obj=None):
        return False

    
    # def has_change_permission(self, request, obj=None):
    #     return False

    def has_delete_permission(self, request, obj=None):
        return False
    

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save_and_continue'] = False
        # extra_context['show_save'] = False
        return super(Registration_FeeAdmin, self).changeform_view(request, object_id, extra_context=extra_context)



admin.site.site_header = 'Comforter CGS Limited Admin'
admin.site.site_title = 'Comforter CGS Limited Admin'
admin.site.index_title = 'Comforter CGS Limited Admin site'