from django.contrib import admin
from django.urls import path
from django.urls import include

from .views import redirect_schedule

urlpatterns = [
    path('', redirect_schedule),
    path('admin/', admin.site.urls),
    path('schedule/', include('schedule.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
]
