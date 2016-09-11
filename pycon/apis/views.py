# -*- coding: UTF-8 -*-
from django.http import HttpResponse, HttpResponseBadRequest, Http404
from django.utils.translation import ugettext as _
import json
from symposion.schedule.models import Schedule, Day, Slot, Presentation
from django.shortcuts import render, get_object_or_404

#Todo::Error処理
def fetch_schedule(slug):
    qs = Schedule.objects.all()
    if slug is None:
        return HttpResponseBadRequest(json.dumps({"error": "HttpResponseBadRequest"}), content_type="application/json")
    else:
        schedule = get_object_or_404(qs, section__slug=slug)
    return schedule

def api_schedule_list(request, slug=None):
    schedule = fetch_schedule(slug)
    presentations = Presentation.objects.filter(section=schedule.section)
    presentations = presentations.exclude(cancelled=True)
    res = []
    #presentation.proposal.language
    for item in presentations:
        tmp = {
            "id": item.pk,
            "title": item.title,
            "category": str(item.proposal.category),
            "description": item.description,
            "language": str(item.proposal.language),
        }
        tmp["speakers"] = [ speaker.name for speaker in item.speakers()]
        if item.slot:
            slot = item.slot
            tmp["day"] = str(slot.day)
            tmp["start"] = str(slot.start)
            tmp["end"] = str(slot.end)
            tmp["rooms"] = str(slot.rooms[0])

        res.append(tmp)
    ctx = {
        "presentations": res,
    }
    return HttpResponse(json.dumps(ctx), content_type="application/json")


def api_presentation_detail(request, pk):
    presentation = get_object_or_404(Presentation, pk=pk)
    res = {
        "id": presentation.pk,
        "title": presentation.title,
        "description": presentation.description,
        "abstract": presentation.abstract,
    }

    speakers = res["speakers"] = []
    speaker_infomations = res["speaker_infomations"] = []

    for speaker in presentation.speakers():
        info = {
            "name": speaker.name,
            "twitter": speaker.twitter_username if speaker.twitter_username else None,
            "image_uri": speaker.photo.url if speaker.photo else None,
        }
        speaker_infomations.append(info)
        speakers.append(speaker.name)

    if presentation.slot:
        slot = presentation.slot
        res["day"] = str(slot.day)
        res["start"] = str(slot.start)
        res["end"] = str(slot.end)
        res["rooms"] = str(slot.rooms[0])
    if presentation.proposal:
        proposal = presentation.proposal
        res["level"] = proposal.get_audience_level_display().encode('utf-8')
        res["category"] = _(proposal.category.name)
        res["language"] = str(proposal.language)

    return HttpResponse(json.dumps(res), content_type="application/json")
