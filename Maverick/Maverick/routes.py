from rest_framework import routers
from django.conf.urls import url,include
from collector.api import resources

router =routers.DefaultRouter()
router.register(r'Scheduler',resources.SchedulerViewset,'ClientsList')
router.register(r'Collector',resources.CollectorViewset,'MarketsList')


urlpatterns = [
    url(r'^', include(router.urls)),
]
