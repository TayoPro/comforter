from django.urls import path
from . views import *


app_name = 'applicants'

urlpatterns = [
    path('', index, name='appli'),
    path('create/profile', CreateProfile.as_view(), name='create_profile1'),
    path('create/profile/step2', CreateProfile2.as_view(), name='create_profile2'),
    path('create/profile/step3', CreateProfile3.as_view(), name='create_profile3'),
    path('create/profile/step4', CreateProfile4.as_view(), name='create_profile4'),
    path('create/profile/step5', CreateProfile5.as_view(), name='create_profile5'),
    path('create/profile/step6', CreateProfile6.as_view(), name='create_profile6'),
    path('applicant/dashboard', ApplicantDashboard.as_view(), name='applicant_dashboard'),
    path('profile', ApplicantProfile.as_view(), name='applicant_profile'),
    path('profile/page2', ApplicantProfile2.as_view(), name='applicant_profile2'),
    path('profile/page3', ApplicantProfile3.as_view(), name='applicant_profile3'),
    path('profile/page4', ApplicantProfile4.as_view(), name='applicant_profile4'),
    path('profile/page5', ApplicantProfile5.as_view(), name='applicant_profile5'),
    path('profile/update', ProfileUpdate.as_view(), name='profile_update'),
    path('profile/update/page2', ProfileUpdate2.as_view(), name='profile_update2'),
    path('profile/update/page3', ProfileUpdate3.as_view(), name='profile_update3'),
    path('profile/update/page4', ProfileUpdate4.as_view(), name='profile_update4'),
    path('profile/update/page5', ProfileUpdate5.as_view(), name='profile_update5'),
    path('all-jobs', DisplayAllJobs.as_view(), name='applicant_all_jobs'),
    path('view-job/<slug:slug>', DisplayJob.as_view(), name='applicant_job'),
    path('apply-to-job/<slug:slug>', JobApply.as_view(), name='applicant_job_apply'),
    path('all-applied-jobs', DisplayAllJobsApplied.as_view(), name='applicant_job_applied'),
    path('all-jobs-shortlisted', DisplayAllJobsSelected.as_view(), name='applicant_jobs_selected'),
    path('notice-removed', JobNoticeRemove.as_view(), name='notice_remove'),
    path('password/update/', ApplicantPassword.as_view(), name='applicant_password'),
    path('application/form/', ApplicantFee.as_view(), name='applicant_payment'),
    path('applicant/payment/', ApplicantPayment.as_view(), name='applicant_pay_fee'),
    path('payment/successful', ApplicantPaid.as_view(), name='applicant_pay_paid'),
    path('search-jobs', applicantsearchemployer, name='applicant_search_employer'),
]
