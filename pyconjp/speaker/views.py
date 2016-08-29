# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.db.models import Q

from symposion.speakers.models import Speaker


def speaker_list(request):
    speakers = Speaker.objects.filter()
    speakers = speakers.exclude(Q(presentations__isnull=True) & Q(copresentations__isnull=True))

    ctx = {
        "speakers": speakers,
    }
    return render(request, "speakers/speaker_list.html", ctx)