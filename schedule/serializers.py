import datetime

from rest_framework import serializers

from django.utils.translation import ugettext as _

from .models import DayPlan
from profiles.models import Profile


class DayPlanSerializer(serializers.ModelSerializer):
    TYPES = (
        (1, _('Locally')),
        (2, _('Work trip')),
        (3, _('Remote work')),
        (4, _('Holiday')),
    )
    changed_by = serializers.CharField(source='worker.user', read_only=True)
    edited = serializers.DateTimeField(read_only=True)

    class Meta:
        model = DayPlan
        fields = "__all__"
