from django.db import models

# Create your models here.


class CompanyProfile(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    keyword = models.CharField(max_length=150, blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    logo = models.ImageField(upload_to='logo', blank=True, null=True)
    favicon = models.ImageField(upload_to='logo', blank=True, null=True, default='logo/favicon-96x96.png')
    banner = models.ImageField(upload_to='logo', blank=True, null=True)
    head_office = models.CharField(max_length=100,blank=True, null=True)
    branch_office1 = models.CharField(max_length=100, blank=True, null=True)
    branch_office2 = models.CharField(max_length=100, blank=True, null=True)
    mobile1 = models.CharField(max_length=20, blank=True, null=True)
    mobile2 = models.CharField(max_length=20, blank=True, null=True)
    mobile3 = models.CharField(max_length=20, blank=True, null=True)
    mobile4 = models.CharField(max_length=20, blank=True, null=True)
    mobile5 = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    about2 = models.TextField(blank=True, null=True)
    about_img = models.ImageField(upload_to='logo', blank=True, null=True, default='logo/aboutus.jpg')
    

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'companyprofile'
        managed = True
        verbose_name = 'CompanyProfile'
        verbose_name_plural = 'CompanyProfile'



class Category(models.Model):
    category_name = models.CharField(max_length=250)
    cat_slug = models.SlugField(blank=True, null=True,  unique=True)

    def __str__(self):
        return self.category_name
    
    class Meta:
        db_table = 'category'
        managed = True
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Service(models.Model):
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=250) 
    slug = models.SlugField(blank=False, null=False,  unique=True)
    job_image = models.ImageField(upload_to='jobs', default='jobs/job.jpg', blank=True, null=True) 
    job_image2 = models.ImageField(upload_to='jobs', blank=True, null=True) 
    job_image3 = models.ImageField(upload_to='jobs', blank=True, null=True) 
    job_image4 = models.ImageField(upload_to='jobs', blank=True, null=True) 
    job_image5 = models.ImageField(upload_to='jobs', blank=True, null=True) 
    job_description = models.TextField(blank=True, null=True)
    list_title = models.CharField(max_length=250, blank=True, null=True)
    list_item1 = models.CharField(max_length=250, blank=True, null=True)
    list_item2 = models.CharField(max_length=250, blank=True, null=True)
    list_item3 = models.CharField(max_length=250, blank=True, null=True)
    list_item4 = models.CharField(max_length=250, blank=True, null=True)
    list_item5 = models.CharField(max_length=250, blank=True, null=True)
    list_item6 = models.CharField(max_length=250, blank=True, null=True)
    list_item7 = models.CharField(max_length=250, blank=True, null=True)
    list_item8 = models.CharField(max_length=250, blank=True, null=True)
    list_item9 = models.CharField(max_length=250, blank=True, null=True)
    list_item10 = models.CharField(max_length=250, blank=True, null=True)
    list2_title = models.CharField(max_length=250, blank=True, null=True)
    list2_item1 = models.CharField(max_length=250, blank=True, null=True)
    list2_item2 = models.CharField(max_length=250, blank=True, null=True)
    list2_item3 = models.CharField(max_length=250, blank=True, null=True)
    list2_item4 = models.CharField(max_length=250, blank=True, null=True)
    list2_item5 = models.CharField(max_length=250, blank=True, null=True)
    list2_item6 = models.CharField(max_length=250, blank=True, null=True)
    list2_item7 = models.CharField(max_length=250, blank=True, null=True)
    list2_item8 = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.category.category_name
    
    class Meta:
        db_table = 'service'
        managed = True
        verbose_name = 'Service'
        verbose_name_plural = 'Services'




STATUS = [
    ('New', 'New'),
    ('Processing', 'Processing'),
    ('Cleared', 'Cleared'),
]

class Contact(models.Model):
    full_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    message = models.TextField()
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)
    cleared = models.DateTimeField(auto_now=True)
    admin_note = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS, default='New')

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = 'contact'
        managed = True 
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
    

class Featured_Company(models.Model):
    c_img = models.ImageField(upload_to='company', blank=True, null=True, default='company/company.png')
  
    class Meta:
        db_table = 'featured_company'
        managed = True
        verbose_name = 'Featured_company'
        verbose_name_plural = 'Featured_companies'



class Registration_Fee(models.Model):
    currency_symbol = models.CharField(max_length=50, blank=True, null=True)
    applicant_fee = models.IntegerField(blank=True, null=True)
    worker_year_fee = models.IntegerField(blank=True, null=True)
    employer_fee = models.IntegerField(blank=True, null=True)
    large_company = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.currency_symbol

    class Meta:
        db_table = 'registration_fee'
        managed = True
        verbose_name = 'Registration_Fee'
        verbose_name_plural = 'Registration_Fees'
    
