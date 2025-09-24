from django.shortcuts import render , redirect
from django.contrib.auth import logout
from jobs.models import *
def home(request):
    jobs = JobPost.objects.filter()[:3]
    if request.user.is_authenticated:

        savedjobs = SavedJob.objects.filter(seeker_id = request.user.id)[:3]
        reco_jobs = JobPost.objects.filter(job_category = request.user.industry)
        ajobs = JobApplication.objects.filter(seeker_id = request.user.id).count() + AcceptedApplication.objects.filter(seeker_id = request.user.id).count() + RejectedApplication.objects.filter(seeker_id = request.user.id).count() 
        sjobs = SavedJob.objects.filter(seeker = request.user).count()
        total = JobPost.objects.all().count
        context = {
            'jobs':jobs,
            'savedjobs': savedjobs,
            'reco_jobs' : reco_jobs,
            'ajobs':ajobs,
            'sjobs':sjobs,
            'savedjobs':savedjobs,
            'total':total,
            
            
        }
        return render(request,'main/home.html',context)
    else:
        return render(request,'main/home.html',{'jobs':jobs})
