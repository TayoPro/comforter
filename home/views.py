from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.db.models import Q
# email message setting 
from django.core.mail import EmailMessage
from django.conf import settings
# email message setting done

from . models import CompanyProfile, Contact, Featured_Company, Service
from createdby.models import CreatedBy
from employers.models import Job_Post
from . forms import ContactForm

# Create your views here.

class IndexList(View):
    def get(self, request):
        home = CompanyProfile.objects.get(pk=1)
        img1 = Featured_Company.objects.get(pk=1)
        img2 = Featured_Company.objects.get(pk=2)
        img3 = Featured_Company.objects.get(pk=3)
        img4 = Featured_Company.objects.get(pk=4)
        img5 = Featured_Company.objects.get(pk=5)
        img6 = Featured_Company.objects.get(pk=6)
        img7 = Featured_Company.objects.get(pk=7)
        img8 = Featured_Company.objects.get(pk=8)
        createdby = CreatedBy.objects.get(pk=1)
        all_job = Job_Post.objects.all().order_by('-id')[:4]
        job_title = Service.objects.all()
        
        return render(request, 'index.html', {
            'home': home,
            'img1': img1,
            'img2': img2,
            'img3': img3,
            'img4': img4,
            'img5': img5,
            'img6': img6,
            'img7': img7,
            'img8': img8,
            'createdby': createdby,
            'all_job': all_job,
            'job_title': job_title,
        })



class MessageList(View):
    def get(self, request):
        talkform = ContactForm()         

        context = {
            'talkform':talkform
        }

        return render(request, 'index.html', context)


    def post(self, request): 
        full_name = request.POST['full_name']
        email_ad = request.POST['email']
        talkform = ContactForm(request.POST) 
        if talkform.is_valid(): 
            talkform.save() 
            messages.success(request, 'Your message is sent successfully! We will contact you shortly.') 
            # email = EmailMessage(
            # 'New message alert!', #title
            # f'This is to notify you that there is a new message from {full_name}. \n Kindly attend to him asap. \n Thank you.', #message body goes here
            # settings.EMAIL_HOST_USER, #sender email
            # [email_ad] #reciever's email
            # )
            # email.fail_silently = True 
            # email.send()
            return redirect('index')





def job_search(request):
    home = CompanyProfile.objects.get(pk=1)
    createdby = CreatedBy.objects.get(pk=1)
    if request.method == 'POST':
        items = request.POST.get('searchbar')
        searched = Q(Q(job__icontains=items)| Q(category__category_name__icontains=items))
        alljob = Job_Post.objects.filter(searched)[:4]
    
    context = {
        'createdby':createdby,
        'items':items,
        'job_searched':alljob,
        'home': home,
    }

    return render(request, 'job_searched.html', context)


def single_service(request, slug):
    home = CompanyProfile.objects.get(pk=1)
    createdby = CreatedBy.objects.get(pk=1)
    service = Service.objects.get(slug=slug)
    
    context = {
        'createdby':createdby,
        'service':service,
    }

    return render(request, 'single_service.html', context)