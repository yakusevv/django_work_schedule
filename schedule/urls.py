from django.urls import path
from django.urls import include

from rest_framework import routers

from .views import ScheduleView, DayPlanViewSet

router = routers.DefaultRouter()
router.register(r'', DayPlanViewSet, basename='day_plans')

urlpatterns = [
    path('', ScheduleView.as_view(), name='schedule_url'),
    path('schedule_api/', include((router.urls, 'day_plans'))),
]
