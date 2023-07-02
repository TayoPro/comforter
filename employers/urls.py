from django.urls import path
from . views import *


app_name = 'employers'

urlpatterns = [
    path('', index, name='empl'),
    path('employer/term', EmployerTerm.as_view(), name='employer_term'),
    path('employer/terms', EmployerTerm2.as_view(), name='employer_term2'),
    # path('employer/terms/fill', EmployerTerm2Refill.as_view(), name='employer_term2_refill'),
    path('employer/make/payment', EmployerMakePayment.as_view(), name='employer_pay'),
    path('employer/payment', EmployerPayment.as_view(), name='employer_payment'),
    path('create/profile', EmployerCreateProfile.as_view(), name='create_profile'),
    path('employer/dashboard', EmployerDashboard.as_view(), name='employer_dashboard'),
    path('employer/profile', EmployerProfile.as_view(), name='employer_profile'),
    path('employer/profile/update', EmployerProfileUpdate.as_view(), name='employer_profile_update'),
    path('employer/password/update', EmployerPassword.as_view(), name='employer_password'),
    path('job/post', JobPost.as_view(), name='job_post'),
    path('job/update/<slug:slug>', JobPostUpdate.as_view(), name='job_post_update'),
    path('jobs/board', JobsBoard.as_view(), name='jobs_board'),
    path('employer/search/', employersearchapplicant, name='employer_search_applicants'),
    path('mark-as-read', ApplicantionNoticeRemoved.as_view(), name='notice_removal'),
    path('all-applicants', AllApplicants.as_view(), name='all_applicants'),
    path('view/applicant/<slug:slug>', ViewApplicant.as_view(), name='view_applicant'),
    path('applicant-pdf/<slug:slug>', employer_applicant_pdf, name='employer_applicant_pdf'),
    path('vacancy/closed/<slug:slug>', Job_Closed.as_view(), name='job_closed'),
    path('shortlist/<slug:slug>', ShortlistApplicant.as_view(), name='shortlist_applicant'),
    path('shortlisted/', ApplicationShortlisted.as_view(), name='shortlisted_applicants'),
    path('hire-/<slug:slug>', HireApplicant.as_view(), name='hire_applicant'),
    path('hired-applicants', HiredApplicants.as_view(), name='hired_applicants'),
    path('decline/<slug:slug>', DeclineApplicant.as_view(), name='decline_applicant'),
    path('resigned/<slug:slug>', EmployeeResigned.as_view(), name='employee_resigned'),
    path('appointment-terminated/<slug:slug>', ApointmentTerminated.as_view(), name='appointment_terminated'),
]
