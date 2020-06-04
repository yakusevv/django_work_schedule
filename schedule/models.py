from django.db import models
from django.utils.translation import ugettext_lazy as _


class DayPlan(models.Model):
    TYPES = (
        (1, _('Locally')),
        (2, _('Work trip')),
        (3, _('Remote work')),
        (4, _('Holiday')),
    )

    worker = models.ForeignKey('profiles.Profile', on_delete=models.CASCADE, related_name=_('work_plan'))
    day = models.DateField(verbose_name=_('Day'))
    note = models.CharField(max_length=50, blank=False, verbose_name=_("Note"))
    type = models.PositiveSmallIntegerField(choices=TYPES)
    changed_by = models.ForeignKey('profiles.Profile', on_delete=models.PROTECT, related_name=_("work_plan_edited"))

    class Meta:
        unique_together = [('worker', 'day'), ]


