from django.shortcuts import render, HttpResponse
from collector import  models

from jobs import clock

# Create your views here.

def index(request):
    data = {}
    data['home'] = 'active'

    return render(request, 'index.html', {'menu': data, })

def scheduler(request):
    data = {}
    data['home'] = 'active'
    return render(request, 'cloud/scheduler.html', {'menu': data, })

def listScheduler(request):
    dataScheduler= models.Scheduler.objects.all()
    data = {'schedulers': dataScheduler}
    return render(request, 'cloud/list-schedulers.html',  data)

def startScheduler(request):
    print("scheduler ")
    clock.startJob()
    return HttpResponse("start")

def pauseScheduler(request):
    print("scheduler ")
    clock._pause()
    return HttpResponse("start")

def resumeScheduler(request):
    print("scheduler ")
    clock._resume()
    return HttpResponse("start")
s
def downScheduler(request):
    print("scheduler ")
    clock._down()
    return HttpResponse("start")

