# -*- coding: utf-8 -*-

from django.contrib import admin

from pyconjp.models import PresentationResource


class PresentationResourceAdmin(admin.ModelAdmin):

    list_display = [
        'id',
        'proposal_base',
        'type',
        'url',
    ]

    class Meta:
        model = PresentationResource

admin.site.register(PresentationResource, PresentationResourceAdmin)
