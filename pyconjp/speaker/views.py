# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.db.models import Q

from symposion.speakers.models import Speaker


def speaker_list(request):
    speakers = Speaker.objects.filter().order_by('name')
    speakers = speakers.exclude(Q(presentations__isnull=True) & Q(copresentations__isnull=True))
    speakers = speakers.exclude(user__isnull=True)
    speakers = speakers.distinct()

    ctx = {
        "speakers": speakers,
    }
    return render(request, "speakers/speaker_list.html", ctx)
