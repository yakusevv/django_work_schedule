import datetime

from django.shortcuts import redirect


def redirect_schedule(request):
    return redirect('schedule_url', year=datetime.datetime.now().year, permanent=True)
