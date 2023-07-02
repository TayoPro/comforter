import requests
import json
import uuid


from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import update_session_auth_hash
from django.template.defaultfilters import slugify
from django.db.models import Q
from django.db import IntegrityError
from django.core.paginator import Paginator
user = get_user_model()
from django.conf import settings
from django.utils import timezone


User = settings.AUTH_USER_MODEL



from . forms import *
from . models import *
from home.models import Registration_Fee, CompanyProfile
from createdby.models import CreatedBy
from employers.models import Job_Post
from home.models import Category
from accounts.models import CustomUser
from accounts.forms import PasswordForm
# Create your views here.


def index(request):
    return HttpResponse('applicants app connected')



class CreateProfile(View):
    def get(self, request):
        home = CompanyProfile.objects.get(pk=1)
        createdby = CreatedBy.objects.get(pk=1)
        form = CreateProfileForm()
        return render(request, 'applicant_create_profile.html', {
            'form':form,
            'home': home,
            'createdby': createdby,
        })

    def post(self, request):
        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            newform = form.save(commit=False)
            newform.user = request.user
            newform.complete = True
            newform.save()
            messages.success(request, 'Step 1 completed! continue with step 2')
            return redirect('applicants:create_profile2')
        else:
            messages.success(request, form.errors)
            return redirect('applicants:create_profile1')


class CreateProfile2(View):
    def get(self, request):
        home = CompanyProfile.objects.get(pk=1)
        createdby = CreatedBy.objects.get(pk=1)
        form = CreateProfileForm2()
        return render(request, 'applicant_create_profile2.html', {
            'form':form,
            'home': home,
            'createdby': createdby,
        })

    def post(self, request):
        form = CreateProfileForm2(request.POST)
        if form.is_valid():
            form.save()
            newform = form.save(commit=False)
            newform.user = request.user
            newform.complete = True
            newform.save()
            messages.success(request, 'Step 2 completed! continue with step 3')
            return redirect('applicants:create_profile3')
        else:
            messages.success(request, form.errors)
            return redirect('applicants:create_profile2')


class CreateProfile3(View):
    def get(self, request):
        home = CompanyProfile.objects.get(pk=1)
        createdby = CreatedBy.objects.get(pk=1)
        form = CreateProfileForm3()
        return render(request, 'applicant_create_profile3.html', {
            'form':form,
            'home': home,
            'createdby': createdby,
        })

    def post(self, request):
        form = CreateProfileForm3(request.POST)
        if form.is_valid():
            form.save()
            newform = form.save(commit=False)
            newform.user = request.user
            newform.complete = True
            newform.save()
            messages.success(request, 'Step 3 completed! continue with step 4')
            return redirect('applicants:create_profile4')
        else:
            messages.success(request, form.errors)
            return redirect('applicants:create_profile3')


class CreateProfile4(View):
    def get(self, request):
        home = CompanyProfile.objects.get(pk=1)
        createdby = CreatedBy.objects.get(pk=1)
        form = CreateProfileForm4()
        return render(request, 'applicant_create_profile4.html', {
            'form':form,
            'home':home,
            'createdby': createdby,
        })

    def post(self, request):
        form = CreateProfileForm4(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            newform = form.save(commit=False)
            newform.user = request.user
            newform.complete = True
            newform.save()
            messages.success(request, 'Step 4 completed! continue with step 5')
            return redirect('applicants:create_profile5')
        else:
            messages.success(request, form.errors)
            return redirect('applicants:create_profile4')


class CreateProfile5(View):
    def get(self, request):
        home = CompanyProfile.objects.get(pk=1)
        createdby = CreatedBy.objects.get(pk=1)
        form = CreateProfileForm5()
        return render(request, 'applicant_create_profile5.html', {
            'form':form,
            'home': home,
            'createdby': createdby,
        })

    def post(self, request):
        form = CreateProfileForm5(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            newform = form.save(commit=False)
            newform.user = request.user
            newform.complete = True
            newform.save()
            messages.success(request, 'Step 5 completed! continue with step 6')
            return redirect('applicants:create_profile6')
        else:
            messages.success(request, form.errors)
            return redirect('applicants:create_profile5')


class CreateProfile6(View):
    def get(self, request):
        fee = Registration_Fee.objects.get(pk=1)
        home = CompanyProfile.objects.get(pk=1)
        createdby = CreatedBy.objects.get(pk=1)
        form = CreateProfileForm()
        return render(request, 'applicant_create_profile6.html', {
            'form': form,
            'fee': fee,
            'home': home,
            'createdby': createdby,
        })

    def post(self, request):
        form = CreateProfileForm6(request.POST)
        if form.is_valid():
            form.save()
            newform = form.save(commit=False)
            newform.user = request.user
            newform.complete = True
            newform.save()
            messages.success(request, 'Step 6 completed! congratulations now you are in')
            return redirect('applicants:applicant_dashboard')
        else:
            messages.success(request, form.errors)
            return redirect('applicants:create_profile6')
        
        

class ApplicantProfile(LoginRequiredMixin, View):
    login_url = 'accounts:applicantsignin'
    def get(self, request):
        home = CompanyProfile.objects.get(pk=1)
        createdby = CreatedBy.objects.get(pk=1)
        profile = General_Information.objects.get(user = request.user)
        return render(request, 'applicant_profile.html', {
            'profile': profile,
            'home': home,
            'createdby': createdby,
        })
        

class ApplicantProfile2(LoginRequiredMixin, View):
    login_url = 'accounts:applicantsignin'
    def get(self, request):
        home = CompanyProfile.objects.get(pk=1)
        createdby = CreatedBy.objects.get(pk=1)
        profile = General_Information.objects.get(user = request.user)
        profile2 = Job_Prospect.objects.get(user = request.user)
        return render(request, 'applicant_profile2.html', {
            'profile': profile,
            'profile2': profile2,
            'home': home,
            'createdby': createdby,
        })
        

class ApplicantProfile3(LoginRequiredMixin, View):
    login_url = 'accounts:applicantsignin'
    def get(self, request):
        home = CompanyProfile.objects.get(pk=1)
        createdby = CreatedBy.objects.get(pk=1)
        profile = General_Information.objects.get(user = request.user)
        profile3 = Health_History.objects.get(user = request.user)
        return render(request, 'applicant_profile3.html', {
            'profile': profile,
            'profile3': profile3,
            'home': home,
            'createdby': createdby,
        })
        

class ApplicantProfile4(LoginRequiredMixin, View):
    login_url = 'accounts:applicantsignin'
    def get(self, request):
        home = CompanyProfile.objects.get(pk=1)
        createdby = CreatedBy.objects.get(pk=1)
        profile = General_Information.objects.get(user = request.user)
        profile4 = Guarantor_Form.objects.get(user = request.user)
        return render(request, 'applicant_profile4.html', {
            'profile': profile,
            'profile4': profile4,
            'home': home,
            'createdby': createdby,
        })
        

class ApplicantProfile5(LoginRequiredMixin, View):
    login_url = 'accounts:applicantsignin'
    def get(self, request):
        home = CompanyProfile.objects.get(pk=1)
        createdby = CreatedBy.objects.get(pk=1)
        profile = General_Information.objects.get(user = request.user)
        profile5 = Guarantor_Form2.objects.get(user = request.user)
        return render(request, 'applicant_profile5.html', {
            'profile': profile,
            'profile5': profile5,
            'home': home,
            'createdby': createdby,
        })

  


# update begins 
class ProfileUpdate(LoginRequiredMixin, View):
    login_url = 'accounts:applicantsignin'
    def get(self, request):
        home = CompanyProfile.objects.get(pk=1)
        createdby = CreatedBy.objects.get(pk=1)
        profile = General_Information.objects.get(user = request.user)
        form = ProfileUpdateForm(instance = request.user.general_information)
        return render(request, 'applicant_profile.html', {
            'form':form,
            'home': home,
            'profile': profile,
            'createdby': createdby,
        })

    def post(self, request):
        form = CreateProfileForm(request.POST, request.FILES, instance = request.user.general_information)
        if form.is_valid():
            update = form.save(commit=False)
            update.user = request.user
            update.save()
            messages.success(request, 'Update successful')
            return redirect('applicants:applicant_profile')
        else:
            messages.error(request, form.errors)
            return redirect('applicants:applicant_profile')


class ProfileUpdate2(LoginRequiredMixin, View):
    login_url = 'accounts:applicantsignin'
    def get(self, request):
        home = CompanyProfile.objects.get(pk=1)
        createdby = CreatedBy.objects.get(pk=1)
        profile = General_Information.objects.get(user=request.user)
        form = ProfileUpdateForm2(instance =request.user.job_prospect)
        return render(request, 'applicant_profile2.html', {
            'form':form,
            'home': home,
            'profile': profile,
            'createdby': createdby,
        })

    def post(self, request):
        form = ProfileUpdateForm2(request.POST, instance =request.user.job_prospect)
        if form.is_valid():
            updated = form.save(commit=False)
            updated.user = request.user
            updated.save()
            messages.success(request, 'Update successful')
            return redirect('applicants:applicant_profile2')
        else:
            messages.error(request, form.errors)
            return redirect('applicants:applicant_profile2')


class ProfileUpdate3(LoginRequiredMixin, View):
    login_url = 'accounts:applicantsignin'
    def get(self, request):
        home = CompanyProfile.objects.get(pk=1)
        createdby = CreatedBy.objects.get(pk=1)
        profile = General_Information.objects.get(user=request.user)
        form = ProfileUpdateForm3(instance =request.user.health_history)
        return render(request, 'applicant_profile3.html', {
            'form':form,
            'home': home,
            'createdby': createdby,
        })

    def post(self, request):
        form = ProfileUpdateForm3(request.POST, instance =request.user.health_history)
        if form.is_valid():
            updated = form.save(commit=False)
            updated.user = request.user
            updated.save()
            messages.success(request, 'Update successful')
            return redirect('applicants:applicant_profile3')
        else:
            messages.success(request, form.errors)
            return redirect('applicants:applicant_profile3')


class ProfileUpdate4(LoginRequiredMixin, View):
    login_url = 'accounts:applicantsignin'
    def get(self, request):
        home = CompanyProfile.objects.get(pk=1)
        createdby = CreatedBy.objects.get(pk=1)
        profile = General_Information.objects.get(user = request.user)
        form = ProfileUpdateForm4(instance =request.user.guarantor_form)
        return render(request, 'applicant_profile4.html', {
            'form':form,
            'home': home,
            'profile': profile,
            'createdby': createdby,
        })

    def post(self, request):
        form = ProfileUpdateForm4(request.POST, request.FILES, instance =request.user.guarantor_form)
        if form.is_valid():
            updated = form.save(commit=False)
            updated.user = request.user
            updated.save()
            messages.success(request, 'Update successful')
            return redirect('applicants:applicant_profile4')
        else:
            messages.success(request, form.errors)
            return redirect('applicants:applicant_profile4')


class ProfileUpdate5(LoginRequiredMixin, View):
    login_url = 'accounts:applicantsignin'
    def get(self, request):
        home = CompanyProfile.objects.get(pk=1)
        createdby = CreatedBy.objects.get(pk=1)
        profile = General_Information.objects.get(user = request.user)
        form = ProfileUpdateForm5(instance =request.user.guarantor_form2)
        return render(request, 'applicant_profile5.html', {
            'form':form,
            'home': home,
            'profile': profile,
            'createdby': createdby,
        })

    def post(self, request):
        form = ProfileUpdateForm5(request.POST, request.FILES, instance =request.user.guarantor_form2)
        if form.is_valid():
            updated = form.save(commit=False)
            updated.user = request.user
            updated.save()
            messages.success(request, 'Update successful')
            return redirect('applicants:applicant_profile5')
        else:
            messages.success(request, form.errors)
            return redirect('applicants:applicant_profile5')





class ApplicantDashboard(LoginRequiredMixin, View):
    login_url = 'accounts:applicantsignin'
    def get(self, request):
        home = CompanyProfile.objects.get(pk=1)
        category = Category.objects.all()
        createdby = CreatedBy.objects.get(pk=1)
        profile = General_Information.objects.get(user = request.user)
        alljobs = Job_Post.objects.all().filter(job_open=True, publish=True).order_by('-id')[:4]
        slugg = Job_Post.objects.all().filter(job_open=True, publish=True)
       
        notice_count = Job_Apply.objects.filter(general_information = profile, shortlisted=True,selected= True, applied=True)
        
        notice_counter = 0
        for item in notice_count:
            notice_counter += item.notice          

        
        return render(request, 'applicant_dashboard.html', {
            'notice_counta':notice_counter,
            'category': category,
            'profile': profile,
            'home': home,
            'createdby': createdby,
            'alljobs': alljobs,
        })



class DisplayAllJobs(LoginRequiredMixin, View):
    login_url = 'accounts:applicantsignin'
    def get(self, request):
        createdby = CreatedBy.objects.get(pk=1)
        category = Category.objects.all()
        profile = General_Information.objects.get(user = request.user)
        alljob = Job_Post.objects.all().filter(job_open=True, publish=True).order_by('-id')
        p = Paginator(alljob, 2)
        page = request.GET.get('page')
        alljobs = p.get_page(page)

        notice_count = Job_Apply.objects.filter(general_information = profile, shortlisted=True, applied=True)
        
        notice_counter = 0
        for item in notice_count:
            notice_counter += item.notice

        return render(request, 'applicant_all_jobs.html',{
            'category': category,
            'profile': profile,
            'createdby': createdby,
            'alljobs': alljobs,
            'notice_counta': notice_counter,
        })


class DisplayJob(LoginRequiredMixin, View):
    login_url = 'accounts:applicantsignin'
    def get(self, request, slug):
        createdby = CreatedBy.objects.get(pk=1)
        category = Category.objects.all()
        profile = General_Information.objects.get(user = request.user)
        update_job = Job_Post.objects.get(slug=slug)

        return render(request, 'applicant_job_apply.html',{
            'category': category,
            'profile': profile,
            'createdby': createdby,
            'update_job': update_job,
        })

    

class JobApply(LoginRequiredMixin, View):
    login_url = 'accounts:applicantsignin'
    def get(self, request, slug):
        update_job = Job_Post.objects.get(slug=slug) 
        profill  = General_Information.objects.get(user = request.user)
        form = JobApplyForm()
        return render(request, 'applicant_job_apply.html',{
            'form': form,
            'update_job': update_job,
            'profill': profill,
        })

    def post(self, request, slug):
        profile  = General_Information.objects.get(user = request.user)
        job_prospt  = Job_Prospect.objects.get(user = request.user)
        health_histry  = Health_History.objects.get(user = request.user)
        update_job = Job_Post.objects.get(slug=slug)    
        try:   
            new_applied = Job_Apply.objects.get(general_information = profile,slug = update_job.slug,applied = True)
            messages.warning(request, 'You can only apply for a job once')
            return redirect('applicants:applicant_all_jobs') 
        except Job_Apply.DoesNotExist:
            form = JobApplyForm(request.POST)
            if form.is_valid():
                newupdate = form.save(commit=False)
                newupdate.category_apply = update_job.category
                newupdate.empl_logo = update_job.employ_logo
                newupdate.employer = update_job.employer_name
                newupdate.previous_company = job_prospt.company_name
                newupdate.language_spoken = health_histry.language_spoken
                newupdate.job_post =  update_job
                newupdate.deadline_date =  update_job.deadline
                newupdate.applied_date = timezone.now()
                newupdate.general_information = profile 
                newupdate.slug = update_job.slug
                newupdate.applied = True
                newupdate.new_applied = True
                newupdate.save()            
                messages.success(request, 'Your job application is successfully submited')
                return redirect('applicants:applicant_job_applied')            
            else:
                messages.success(request, form.errors)
                return redirect('applicants:applicant_all_jobs')
        # except IntegrityError:
      



class DisplayAllJobsApplied(LoginRequiredMixin, View):
    login_url = 'accounts:applicantsignin'
    def get(self, request):
        createdby = CreatedBy.objects.get(pk=1)
        category = Category.objects.all()
        profile = General_Information.objects.get(user = request.user)
        alljob = Job_Apply.objects.filter(general_information = profile, applied=True).order_by('id')
        p = Paginator(alljob, 2)
        page = request.GET.get('page')
        alljobs = p.get_page(page)

        notice_count = Job_Apply.objects.filter(general_information = profile, shortlisted=True,selected=True, applied=True)
        
        notice_counter = 0
        for item in notice_count:
            notice_counter += item.notice


        return render(request, 'applicant_jobs_applied.html',{
            'category': category,
            'profile': profile,
            'createdby': createdby,
            'alljobs': alljobs,
            'notice_counta': notice_counter,
        })



class DisplayAllJobsSelected(LoginRequiredMixin, View):
    login_url = 'accounts:applicantsignin'
    def get(self, request):
        createdby = CreatedBy.objects.get(pk=1)
        category = Category.objects.all()
        profile = General_Information.objects.get(user = request.user)
        alljob = Job_Apply.objects.filter(general_information = profile, selected=True, applied=True).order_by('id')
        p = Paginator(alljob, 2)
        page = request.GET.get('page')
        alljobs = p.get_page(page)

        notice_count = Job_Apply.objects.filter(general_information = profile, selected=True, shortlisted=True, applied=True)
        
        notice_counta = 0
        for item in notice_count:
            notice_counta += item.notice

        return render(request, 'applicant_job_notice.html',{
            'category': category,
            'profile': profile,
            'createdby': createdby,
            'alljobs': alljobs,
            'notice_counta': notice_counta,
        })



class JobNoticeRemove(View):
    def post(self, request):
        profile = General_Information.objects.get(user = request.user)
        alljob = Job_Apply.objects.filter(general_information = profile, selected=True, shortlisted=True, applied=True)
        for item in alljob:
            item.shortlisted = False
            item.save()
        
        return redirect('applicants:applicant_jobs_selected')


class ApplicantPassword(LoginRequiredMixin, View):
    login_url = 'applicants:applicantsignin'
    def get(self, request):
        profile = General_Information.objects.get(user = request.user)
        createdby = CreatedBy.objects.get(pk=1)
        form = PasswordForm(request.user)

        context = {
            'form': form,
            'profile': profile,
            'createdby': createdby,
        }
        return render(request, 'applicant_profile_password.html', context)


    def post(self, request):
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password change is successful.')
            return redirect('applicants:applicant_dashboard')
        else:
            messages.error(request, form.errors)
            return redirect('applicants:applicant_password')

    


class ApplicantFee(LoginRequiredMixin, View):
    login_url = 'applicants:applicantsignin'
    def get(self, request):
        profile = General_Information.objects.get(user = request.user)
        createdby = CreatedBy.objects.get(pk=1)
        fee = Registration_Fee.objects.get(pk=1)

        context= {
            'profile':profile,
            'createdby':createdby,
            'fee':fee,
        }
        return render(request, 'applicant_payment.html', context)



class ApplicantPayment(View):
    def post(self, request):
        api_key = 'sk_test_0c3bb25f14513ee95dcbe057e8b007f8b8480aa1'
        curl = 'https://api.paystack.co/transaction/initialize'
        cburl = 'http://16.170.248.85/applicants/payment/successful'
        # cburl = 'http://localhost:8000/applicants/payment/successful'
        ref = str(uuid.uuid4())
        amount = float(request.POST['total']) * 100
        employ_no = request.user.id
        email = request.user.email
        user = request.user
        phone = request.POST['phone_no']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        headers = {'Authorization': f'Bearer {api_key}'}
        data = {'reference': ref, 'amount': int(amount), 'email': email, 'order_number': employ_no, 'callback_url': cburl, 'currency': 'NGN'}

        try:
            r = requests.post(curl, headers=headers, json= data)
            messages.success(request, 'paymeny successful!')
        except Exception:
            messages.error(request, 'Network busy')
        else:   
            transback = json.loads(r.text)
            rurl = transback['data']['authorization_url']

            form = ApplicantPaymentForm(request.POST)
            if form.is_valid():
                account = form.save(commit=False)
                account.user = user
                account.first_name = first_name
                account.last_name = last_name
                account.total = amount/100
                account.applicant_number = employ_no
                account.pay_code = ref
                account.phone_no = phone
                account.paid = True
                account.complete = True
                account.save()

            # email = EmailMessage(
            #     'Transaction Completed!', 
            #     f'Dear {user.first_name}, your transaction is completed. \n Your order will be delivered in 24hours. \n Thank you for your patronage.', #message body goes here
            #     settings.EMAIL_HOST_USER, 
            #     [email] 
            # )

            # email.fail_silently = True 
            # email.send()

            return redirect(rurl)
        return redirect('applicants:applicant_payment')



class ApplicantPaid(View):
    def get(self, request):
        profile = General_Information.objects.get(user = request.user)
        createdby = CreatedBy.objects.get(pk=1)

        context = {
            'profile':profile,
            'createdby':createdby,
        }
        return render(request, 'applicant_paid.html', context)




@login_required(login_url='applicants:applicantsignin')
def applicantsearchemployer(request):
    createdby = CreatedBy.objects.get(pk=1)
    category = Category.objects.all()
    profile = General_Information.objects.get(user = request.user)
    if request.method == 'POST':
        items = request.POST.get('searchbar')
        items2 = request.POST.get('searchbar2')
        searched = Q(Q(job__icontains=items)| Q(category__category_name__icontains=items2))
        job_searched = Job_Post.objects.filter(searched)
        p = Paginator(job_searched, 3)
        page = request.GET.get('page')
        alljobs = p.get_page(page)
    
    context = {
        'category':category,
        'createdby':createdby,
        'profile':profile,
        'items':items,
        'items2':items2,
        'alljobs':alljobs
    }

    return render(request, 'applicants_search_employer.html', context)