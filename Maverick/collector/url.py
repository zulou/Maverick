from django.conf.urls import url,include
from django.contrib.auth.views import logout
from . import views

urlpatterns = [


    url(r'^index/', views.index, name='index'),
    url(r'^scheduler/', views.scheduler, name='scheduler'),
    url(r'^startScheduler/', views.startScheduler, name='startScheduler'),
    url(r'^pauseScheduler/', views.pauseScheduler, name='pauseScheduler'),
    url(r'^resumeScheduler/', views.resumeScheduler, name='resumeScheduler'),
    url(r'^downScheduler/', views.downScheduler, name='downScheduler'),
    url(r'^listScheduler/', views.listScheduler, name='listScheduler'),
    #url(r'^', views.index, name='index'),

]
