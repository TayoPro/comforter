import requests
import json
import uuid

from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.views import View
from django.contrib import messages
from django.template.defaultfilters import slugify
from django.db.models import Q
from django.db import IntegrityError
from django.core.paginator import Paginator

#to convert to pdf file pip install xhtml2pdf also create pdf.py file and import it here as below
from .pdf import applicant2pdf


from home.models import CompanyProfile,Registration_Fee
from createdby.models import CreatedBy
from . models import *
from applicants.models import Job_Apply, General_Information
from applicants.forms import JobApplyForm
from . forms import EmployerCreateProfileForm, Employer_ProfileUpdateForm, JobPostForm, JobPostUpdateForm, EmployerTermForm, EmployerTerms2Form,EmployerPaymentForm
from accounts.forms import PasswordForm
from django.utils import timezone
from home.models import Category
# Create your views here.

def index(request):
    return HttpResponse('employer done')


class EmployerTerm(View):
    def get(self, request):
        createdby = CreatedBy.objects.get(pk=1)
        home = CompanyProfile.objects.get(pk=1)
        regfee = Registration_Fee.objects.get(pk=1)
        form = EmployerTermForm()
        return render(request, 'employer_terms.html', {
            'createdby':createdby,
            'form':form, 
            'regfee':regfee,
            'home':home,
            })

    def post(self, request):
        form = EmployerTermForm(request.POST)
        if form.is_valid():
            newterm= form.save(commit=False)
            try:
                newterm.user = request.user
                newterm.complete = True
                newterm.save()
                messages.success(request, 'Successfully submited!')
                return redirect('employers:employer_term2')
            except IntegrityError:
                messages.success(request, 'Sign in to your dashboard.')
                return redirect('accounts:employersignin')
        else:
            messages.error(request, form.errors)
            return redirect('employers:employer_term')


class EmployerTerm2(View):
    def get(self, request):
        createdby = CreatedBy.objects.get(pk=1)
        home = CompanyProfile.objects.get(pk=1)
        regfee = Registration_Fee.objects.get(pk=1)
        form = EmployerTerms2Form()
        return render(request, 'employer_terms2.html', {
            'createdby':createdby, 
            'form':form, 
            'home':home, 
            'regfee':regfee,
            })

    def post(self, request):
        form = EmployerTerms2Form(request.POST)
        if form.is_valid():
            newterm= form.save(commit=False)
            try:
                newterm.user = request.user
                newterm.complete = True
                newterm.save()
                messages.success(request, 'Successful')
                return redirect('employers:employer_pay')
            except IntegrityError:
                messages.success(request, 'Sign in to your dashboard.')
                return redirect('accounts:employersignin')
        else:
            messages.error(request, form.errors)
            return redirect('employers:employer_term2')

        
class EmployerMakePayment(View):
    def get(self, request):
        createdby = CreatedBy.objects.get(pk=1)
        home = CompanyProfile.objects.get(pk=1)
        regfee = Registration_Fee.objects.get(pk=1)
        phone = EmployerTerms2.objects.get(user= request.user)
        return render(request, 'employer_pay.html', {
            'createdby':createdby,
            'home':home,
            'regfee':regfee,
            'phone':phone,
        })
        

class EmployerPayment(View):
    def post(self, request):
        api_key = 'sk_test_0c3bb25f14513ee95dcbe057e8b007f8b8480aa1'
        curl = 'https://api.paystack.co/transaction/initialize'
        # cburl = 'http://16.170.248.85/employers/create/profile'
        cburl = 'http://localhost:8000/employers/create/profile'
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
            messages.success(request, 'registration successful!')
        except Exception:
            messages.error(request, 'Network busy')
        else:   
            transback = json.loads(r.text)
            rurl = transback['data']['authorization_url']

            form = EmployerPaymentForm(request.POST)
            if form.is_valid():
                account = form.save(commit=False)
                account.user = user
                account.first_name = first_name
                account.last_name = last_name
                account.total = amount/100
                account.employer_number = employ_no
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
        return redirect('employers:employer_term2')



class EmployerCreateProfile(LoginRequiredMixin, View):
    login_url = 'employers:employersignin'
    def get(self, request):
        createdby = CreatedBy.objects.get(pk=1)
        home = CompanyProfile.objects.get(pk=1)
        form = EmployerCreateProfileForm()

        context = {
            'createdby':createdby,
            'home':home,
        }
        return render(request, 'employer_create_profile.html', context)

    def post(self, request):
        form = EmployerCreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            paid = form.save(commit=False)
            try:
                paid.user = request.user
                paid.complete = True
                paid.save()
                messages.success(request, 'Membership registration successful!')
                return redirect('employers:employer_dashboard')
            except IntegrityError:
                messages.success(request, 'Sign in to your dashboard.')
                return redirect('accounts:employersignin')
                # return redirect('employers:employer_dashboard')
        else:
            messages.error(request, form.errors)
            return redirect('employers:create_profile')



class EmployerProfile(LoginRequiredMixin, View):
    login_url = 'employers:employersignin'
    def get(self, request):
        createdby = CreatedBy.objects.get(pk=1)
        emprofile = Employer_Profile.objects.get(user = request.user)

        context = {
            'createdby':createdby,
            'emprofile':emprofile,
        }
        return render(request, 'employer_profile.html', context)



class EmployerProfileUpdate(LoginRequiredMixin, View):
    login_url = 'employers:employersignin'
    def get(self, request):
        home = CompanyProfile.objects.get(pk=1)
        createdby = CreatedBy.objects.get(pk=1)
        emprofile = Employer_Profile.objects.get(user = request.user)
        form = Employer_ProfileUpdateForm(instance =request.user.employer_profile)
        return render(request, 'employer_profile_update.html', {
            'form':form,
            'home': home,
            'emprofile': emprofile,
            'createdby': createdby,
        })

    def post(self, request):
        form = Employer_ProfileUpdateForm(request.POST, request.FILES, instance =request.user.employer_profile)
        if form.is_valid():
            updated = form.save(commit=False)
            updated.user = request.user
            updated.save()
            messages.success(request, 'Profile updated successful')
            return redirect('employers:employer_profile')
        else:
            messages.success(request, form.errors)
            return redirect('employers:employer_profile_update')




class EmployerPassword(LoginRequiredMixin, View):
    login_url = 'employers:employersignin'
    def get(self, request):
        emprofile = Employer_Profile.objects.get(user = request.user)
        createdby = CreatedBy.objects.get(pk=1)
        form = PasswordForm(request.user)

        context = {
            'form': form,
            'emprofile': emprofile,
            'createdby': createdby,
        }
        return render(request, 'employer_profile_password.html', context)


    def post(self, request):
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password change is successful.')
            return redirect('employers:employer_dashboard')
        else:
            messages.error(request, form.errors)
            return redirect('employers:employer_password')

    


class JobPost(LoginRequiredMixin, View):
    login_url = 'employers:employersignin'
    def get(self, request):
        home = CompanyProfile.objects.get(pk=1)
        createdby = CreatedBy.objects.get(pk=1)
        category = Category.objects.all()
        emprofile = Employer_Profile.objects.get(user = request.user)
        form = JobPostForm()
        return render(request, 'employer_job_post.html.', {
            'form':form,
            'home': home,
            'emprofile': emprofile,
            'createdby': createdby,
            'category': category,
        })

    def post(self, request):
        profile = request.POST.get('profile')
        deprofile  = Employer_Profile.objects.get(id = profile)
        cat_id = request.POST.get('category_id')
        decat_id  = Category.objects.get(id = cat_id)
        getnum = Job_Post.objects.filter(employer_profile= deprofile).last()
        if getnum:
            new_num = getnum.id
            de_id = new_num + 1
        else:
            de_id = 1
            
        form = JobPostForm(request.POST)
        if form.is_valid():
            updated = form.save(commit=False)
            updated.job_open = True
            updated.category = decat_id
            updated.employer_profile = deprofile
            updated.employ_logo = deprofile.employer_logo
            updated.employer_name = deprofile.company_name
            updated.num_alpha = deprofile.company_name + '-' + updated.job + '-' + str(de_id)
            updated.slug = slugify(updated.num_alpha).lower()
            updated.save()
            messages.success(request, 'Job Post successful')
            return redirect('employers:jobs_board')
        else:
            messages.success(request, form.errors)
            return redirect('employers:job_post')


class JobPostUpdate(LoginRequiredMixin, View):
    login_url = 'employers:employersignin'
    def get(self, request, slug):
        home = CompanyProfile.objects.get(pk=1)
        createdby = CreatedBy.objects.get(pk=1)
        category = Category.objects.all()
        emprofile = Employer_Profile.objects.get(user = request.user)
        update_job = Job_Post.objects.get(slug=slug)
        form = JobPostUpdateForm(instance = update_job)
        return render(request, 'employer_job_post_update.html.', {
            'form':form,
            'home': home,
            'emprofile': emprofile,
            'createdby': createdby,
            'update_job': update_job,
            'category': category,
        })

    def post(self, request, slug):
        profile = request.POST.get('profile')
        deprofile  = Employer_Profile.objects.get(id = profile)
        update_job = Job_Post.objects.get(slug=slug)
        cat_id = request.POST.get('category_id')
        decat_id  = Category.objects.get(id = cat_id)
        form = JobPostUpdateForm(request.POST, instance = update_job)
        if form.is_valid():
            newupdate = form.save(commit=False)
            newupdate.job_open = True
            newupdate.job_updated =  timezone.now() 
            newupdate.category = decat_id
            newupdate.employer_profile = deprofile
            newupdate.employ_logo = deprofile.employer_logo
            newupdate.employer_name = deprofile.company_name
            newupdate.num_alpha =  deprofile.company_name + '-' + newupdate.job + '-' + str(newupdate.id).lower()
            newupdate.slug = slugify(updated.num_alpha).lower()
            newupdate.save()
            messages.success(request, 'Job post update is successful')
            return redirect('employers:jobs_board')
        else:
            messages.success(request, form.errors)
            return redirect('employers:job_post_update')




class EmployerDashboard(LoginRequiredMixin, View):
    login_url = 'employers:employersignin'
    def get(self, request):
        category = Category.objects.all()
        emprofile = Employer_Profile.objects.get(user = request.user)
        createdby = CreatedBy.objects.get(pk=1)
        job_profile = Job_Post.objects.filter(employer_profile = emprofile).first()
        if job_profile:
            allapply = Job_Apply.objects.filter(employer = job_profile.employer_name, applied=True).order_by('id')[:4]
        else:
            allapply = Job_Apply.objects.filter(employer = job_profile, applied=True).order_by('id')[:4]
        if job_profile:
            notice_count = Job_Apply.objects.filter(employer = job_profile.employer_name, new_applied=True, applied=True)
            notice_counter = 0
            if notice_count:
                for item in notice_count:
                    notice_counter += item.notice       
        else:
            notice_counter = 0


        context = {
            'category':category,
            'createdby':createdby,
            'emprofile':emprofile,
            'allapply':allapply,
            'notice_counter':notice_counter,
        }
        return render(request, 'employer_dashboard.html', context)




class JobsBoard(LoginRequiredMixin, View):
    login_url = 'employers:employersignin'
    def get(self, request):
        category = Category.objects.all()
        createdby = CreatedBy.objects.get(pk=1)
        emprofile = Employer_Profile.objects.get(user = request.user)
        job_profile = Employer_Profile.objects.filter(user = request.user).first()
        all_job = Job_Post.objects.filter(employer_profile= job_profile, publish= True).order_by('-id')
        p = Paginator(all_job, 3)
        page = request.GET.get('page')
        all_jobs = p.get_page(page)

        context = {
            'category':category,
            'all_jobs':all_jobs,
            'emprofile':emprofile,
            'createdby':createdby,
        }
        return render(request, 'employer_jobs_board.html', context)


@login_required(login_url='employers:employersignin')
def employersearchapplicant(request):
    createdby = CreatedBy.objects.get(pk=1)
    category = Category.objects.all()
    emprofile = Employer_Profile.objects.get(user = request.user)
    if request.method == 'POST':
        items = request.POST.get('searchbar')
        items2 = request.POST.get('searchbar2')
        searched = Q(Q(job__icontains=items)| Q(category_apply__icontains=items2))
        applicant_searched = Job_Apply.objects.filter(searched)
        p = Paginator(applicant_searched, 3)
        page = request.GET.get('page')
        all_jobs = p.get_page(page)
    
    context = {
        'category':category,
        'createdby':createdby,
        'emprofile':emprofile,
        'items':items,
        'items2':items2,
        'all_jobs':all_jobs
    }

    return render(request, 'employer_search_applicants.html', context)




class ApplicantionNoticeRemoved(View):
    def post(self, request):
        emprofile = Employer_Profile.objects.get(user = request.user)
        job_profile = Job_Post.objects.filter(employer_profile = emprofile).first()
        alljob = Job_Apply.objects.filter(employer = job_profile.employer_name, new_applied=True,applied=True)
        for item in alljob:
            item.new_applied = False
            item.save()
        
        return redirect('employers:all_applicants')



class AllApplicants(LoginRequiredMixin, View):
    login_url = 'employers:employersignin'
    def get(self, request):
        createdby = CreatedBy.objects.get(pk=1)
        category = Category.objects.all()
        emprofile = Employer_Profile.objects.get(user = request.user)
        job_profile = Job_Post.objects.filter(employer_profile = emprofile).first()
        if job_profile:
            alljob = Job_Apply.objects.filter(employer = job_profile.employer_name,  applied=True).order_by('id')
        else:
            alljob = Job_Apply.objects.filter(employer = job_profile,  applied=True).order_by('id')
        p = Paginator(alljob, 2)
        page = request.GET.get('page')
        all_jobs = p.get_page(page)

        if job_profile:
            notice_count = Job_Apply.objects.filter(employer = job_profile.employer_name, new_applied=True, applied=True)
            notice_counter = 0
            if notice_count:
                for item in notice_count:
                    notice_counter += item.notice       
        else:
            notice_counter = 0

        return render(request, 'employer_all_applicants.html',{
            'category': category,
            'emprofile': emprofile,
            'createdby': createdby,
            'all_jobs': all_jobs,
            'notice_counter': notice_counter,
        })



class ViewApplicant(LoginRequiredMixin, View):
    login_url = 'employers:employersignin'
    def get(self, request, slug):
        emprofile = Employer_Profile.objects.get(user = request.user)
        view_job = Job_Apply.objects.get(slug = slug)      

        context = {
            'emprofile':emprofile,
            'view_job':view_job,
        }
        return render(request, 'employer_view_applicant.html', context)


def employer_applicant_pdf(request, slug):
    emprofile = Employer_Profile.objects.get(user = request.user)
    view_job = Job_Apply.objects.get(slug = slug) 
    pdf = applicant2pdf("employer_applicant_pdf.html", {'emprofile':emprofile,'view_job':view_job})

    return HttpResponse(pdf, content_type = "application/pdf")

    



class Job_Closed(LoginRequiredMixin, View):
    login_url = 'employers:employersignin'
    def post(self, request, slug):
        emprofile = Employer_Profile.objects.get(user = request.user)
        view_job = Job_Post.objects.get(slug = slug) 
        if view_job:
            view_job.job_closed = True
            view_job.job_open = False
            view_job.job_closed_date = timezone.now() 
            view_job.save()
            messages.success(request, f'Vacancy for {view_job.job} closed')
            return redirect('employers:jobs_board')
        else:
            messages.warning(request, 'Applicant is not shortlisted')
            return redirect('employers:jobs_board')


class ShortlistApplicant(LoginRequiredMixin, View):
    login_url = 'employers:employersignin'
    def post(self, request, slug):
        emprofile = Employer_Profile.objects.get(user = request.user)
        view_job = Job_Apply.objects.get(slug = slug) 
        if view_job:
            view_job.shortlisted = True
            view_job.selected = True
            view_job.resigned = False
            view_job.terminated = False
            view_job.hired = False
            view_job.declined = False
            view_job.shortlisted_date = timezone.now()
            view_job.save()
            messages.success(request, 'The applicant has been successfully shortlisted')
            return redirect('employers:shortlisted_applicants')
        else:
            messages.warning(request, 'Applicant is not shortlisted')
            return redirect('employers:all_applicants')


class ApplicationShortlisted(LoginRequiredMixin, View):
    login_url = 'employers:employersignin'
    def get(self, request):
        category = Category.objects.all()
        createdby = CreatedBy.objects.get(pk=1)
        emprofile = Employer_Profile.objects.get(user = request.user)
        job_profile = Job_Post.objects.filter(employer_profile = emprofile).first()
        if job_profile:
            alljob = Job_Apply.objects.filter(employer = job_profile.employer_name, shortlisted=True,  applied=True).order_by('id')
        else:
            alljob = Job_Apply.objects.filter(employer = job_profile, shortlisted=True,  applied=True).order_by('id')
        p = Paginator(alljob, 2)
        page = request.GET.get('page')
        all_jobs = p.get_page(page)

        if job_profile:
            notice_count = Job_Apply.objects.filter(employer = job_profile.employer_name, new_applied=True, applied=True)
            notice_counter = 0
            if notice_count:
                for item in notice_count:
                    notice_counter += item.notice       
        else:
            notice_counter = 0

        return render(request, 'employer_applicants_shortlisted.html ',{
            'category': category,
            'emprofile': emprofile,
            'createdby': createdby,
            'all_jobs': all_jobs,
            'notice_counter': notice_counter,
        })


class HireApplicant(LoginRequiredMixin, View):
    login_url = 'employers:employersignin'
    def post(self, request, slug):
        emprofile = Employer_Profile.objects.get(user = request.user)
        view_job = Job_Apply.objects.get(slug = slug) 
        if view_job:
            view_job.hired = True
            view_job.shortlisted = False
            view_job.resigned = False
            view_job.terminated = False
            view_job.hireded_date = timezone.now()
            view_job.save()
            messages.success(request, 'The candidate has been successfully hired')
            return redirect('employers:hired_applicants')
        else:
            messages.warning(request, 'Applicant not hired yet')
            return redirect('employers:shortlisted_applicants')


class HiredApplicants(LoginRequiredMixin, View):
    login_url = 'employers:employersignin'
    def get(self, request):
        category = Category.objects.all()
        createdby = CreatedBy.objects.get(pk=1)
        emprofile = Employer_Profile.objects.get(user = request.user)
        job_profile = Job_Post.objects.filter(employer_profile = emprofile).first()
        if job_profile:
            alljob = Job_Apply.objects.filter(employer = job_profile.employer_name, hired=True,  applied=True).order_by('id')
        else:
            alljob = Job_Apply.objects.filter(employer = job_profile, hired=True,  applied=True).order_by('id')
        p = Paginator(alljob, 2)
        page = request.GET.get('page')
        all_jobs = p.get_page(page)
        
        if job_profile:
            notice_count = Job_Apply.objects.filter(employer = job_profile.employer_name, new_applied=True, applied=True)
            notice_counter = 0
            if notice_count:
                for item in notice_count:
                    notice_counter += item.notice       
        else:
            notice_counter = 0
            
        return render(request, 'employer_all_hired.html ',{
            'category': category,
            'emprofile': emprofile,
            'createdby': createdby,
            'all_jobs': all_jobs,
            'notice_counter': notice_counter,
        })



class DeclineApplicant(LoginRequiredMixin, View):
    login_url = 'employers:employersignin'
    def post(self, request, slug):
        emprofile = Employer_Profile.objects.get(user = request.user)
        view_job = Job_Apply.objects.get(slug = slug) 
        if view_job:
            view_job.declined = True
            view_job.hired = False
            view_job.shortlisted = False
            view_job.resigned = False
            view_job.terminated = False
            view_job.declined_date = timezone.now()
            view_job.save()
            messages.success(request, 'Declined')
            return redirect('employers:hired_applicants')
        else:
            messages.warning(request, 'Applicant not hired yet')
            return redirect('employers:shortlisted_applicants')


class EmployeeResigned(LoginRequiredMixin, View):
    login_url = 'employers:employersignin'
    def post(self, request, slug):
        emprofile = Employer_Profile.objects.get(user = request.user)
        view_job = Job_Apply.objects.get(slug = slug) 
        if view_job:
            view_job.resigned = True
            view_job.shortlisted = False
            view_job.terminated = False
            view_job.resigned_date = timezone.now()
            view_job.save()
            messages.success(request, f'{view_job.general_information.first_name} {view_job.general_information.last_name} has resigned from his appointment.')
            return redirect('employers:hired_applicants')
        else:
            messages.warning(request, 'Applicant not hired yet')
            return redirect('employers:all_applicants')




class ApointmentTerminated(LoginRequiredMixin, View):
    login_url = 'employers:employersignin'
    def post(self, request, slug):
        emprofile = Employer_Profile.objects.get(user = request.user)
        view_job = Job_Apply.objects.get(slug = slug) 
        if view_job:
            view_job.terminated = True
            view_job.resigned = False
            view_job.shortlisted = False
            view_job.terminated_date = timezone.now()
            view_job.save()
            messages.success(request, f'{view_job.general_information.first_name} {view_job.general_information.last_name} appointment has been terminated.')
            return redirect('employers:hired_applicants')
        else:
            messages.warning(request, 'Applicant not hired yet')
            return redirect('employers:all_applicants')


