from django.shortcuts import redirect


def redirect_schedule(request):
    return redirect('schedule_url', permanent=True)
