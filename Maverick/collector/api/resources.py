from rest_framework import viewsets
from collector import models
from . import serializers

class SchedulerViewset(viewsets.ModelViewSet):
	queryset=models.Scheduler.objects.all()
	serializer_class=serializers.Schedulerserializer

class CollectorViewset(viewsets.ModelViewSet):
    queryset = models.Collector.objects.all()
    serializer_class = serializers.Collectorserializer
