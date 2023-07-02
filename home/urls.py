from django.urls import path
from . views import *



urlpatterns = [
    path('', IndexList.as_view(), name='index'),
    path('message', MessageList.as_view(), name='message'),
    path('job/search', job_search, name='job_search'),
    path('services/<slug:slug>', single_service, name='single_service'),
]