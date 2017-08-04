# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from symposion.proposals.models import ProposalBase


class PresentationResource(models.Model):
    PRESENTATION_RESOURCE_TYPE = (
        ('video', _('Video')),
        ('slide', _('Slide')),
        ('code', _('Code')),
    )

    proposal_base = models.ForeignKey(ProposalBase, related_name="presentation_resources")
    url = models.CharField(max_length=1024)
    type = models.CharField(
        max_length=16,
        choices=PRESENTATION_RESOURCE_TYPE,
    )
    label = models.CharField(max_length=16, default='', blank=True)

    def __unicode__(self):
        return u"<#{}, {}, '{}'>".format(
            self.pk, self.type, self.url,
        )
