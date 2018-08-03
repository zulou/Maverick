from django.db import models
from django.utils import timezone
#import datetime

# Create your models here.

class Scheduler(models.Model):
    date = models.DateTimeField(default=timezone.now)
    state = models.IntegerField(default=1,blank=False)
    type = models.IntegerField(default=1,blank=False)
    description=models.CharField(max_length=50,blank=True)
    def __str__(self):
        return(str(self.date)+" estado:"+str(self.state))

class Collector (models.Model):
    scheduler=models.ForeignKey(Scheduler,on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    data=models.TextField(null=True, blank=True)
    def __str__(self):
        return(str(self.scheduler)+" "+str(self.date)+""+str(self.type)+":"+str(self.data))





