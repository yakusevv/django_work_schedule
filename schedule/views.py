from django.views.generic import TemplateView

from profiles.models import Profile


class ScheduleView(TemplateView):
    template_name = 'schedule/schedule_view.html'

    def get_context_data(self, **kwargs):
        context = super(ScheduleView, self).get_context_data()
        context['Workers'] = Profile.objects.all()
