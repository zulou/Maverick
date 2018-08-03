from rest_framework import serializers

from collector  import models

class Schedulerserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Scheduler
        fields = ('id','date','state','type','description')

class Collectorserializer(serializers.HyperlinkedModelSerializer):
    scheduler = serializers.PrimaryKeyRelatedField(many=False, queryset=models.Scheduler.objects.all())
    class Meta:
        model = models.Collector
        fields = ('id', 'scheduler','date','data')




