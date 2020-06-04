import datetime

from calendar import monthlen

from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import redirect

from rest_framework import viewsets, permissions

from .serializers import DayPlanSerializer
from .models import DayPlan

from profiles.models import Profile


class ScheduleView(TemplateView):
    template_name = 'schedule/schedule_view.html'

    def get(self, request):
        if not self.request.GET.get('year'):
            response = redirect('schedule_url')
            response['Location'] += '?year={}'.format(datetime.datetime.now().year)
            return response
        else:
            context = self.get_context_data()
            return render(request, self.template_name, context=context)

    def get_context_data(self, **kwargs):
        context = super(ScheduleView, self).get_context_data()
        year = int(self.request.GET.get('year'))

        context['Workers'] = Profile.objects.all()
        context['Year'] = year
        context['Months'] = {
            _("January"): [datetime.date(year, 1, day) for day in range(1, monthlen(year, 1)+1)],
            _("February"): [datetime.date(year, 2, day) for day in range(1, monthlen(year, 2)+1)],
            _("March"): [datetime.date(year, 3, day) for day in range(1, monthlen(year, 3)+1)],
            _("April"): [datetime.date(year, 4, day) for day in range(1, monthlen(year, 4)+1)],
            _("May"): [datetime.date(year, 5, day) for day in range(1, monthlen(year, 5)+1)],
            _("June"): [datetime.date(year, 6, day) for day in range(1, monthlen(year, 6)+1)],
            _("July"): [datetime.date(year, 7, day) for day in range(1, monthlen(year, 7)+1)],
            _("August"): [datetime.date(year, 8, day) for day in range(1, monthlen(year, 8)+1)],
            _("September"): [datetime.date(year, 9, day) for day in range(1, monthlen(year, 9)+1)],
            _("October"): [datetime.date(year, 10, day) for day in range(1, monthlen(year, 10)+1)],
            _("November"): [datetime.date(year, 11, day) for day in range(1, monthlen(year, 11)+1)],
            _("December"): [datetime.date(year, 12, day) for day in range(1, monthlen(year, 12)+1)],
        }
        return context


class DayPlanViewSet(viewsets.ModelViewSet):
    queryset = DayPlan.objects.all()
    serializer_class = DayPlanSerializer
    permission_classes = (permissions.IsAdminUser,)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.validated_data['edited'] = datetime.datetime.now()
            serializer.validated_data['changed_by'] = self.request.user.profile
            serializer.save()
