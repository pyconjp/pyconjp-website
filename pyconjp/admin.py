# -*- coding: utf-8 -*-

from django.contrib import admin
from django import forms
from django.db.models import ObjectDoesNotExist

from pyconjp.models import PresentationResource
from symposion.proposals.models import ProposalBase


class PresentationChoideField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        """
        プロポーザル名のドロップダウン表示をカスタマイズ
        """
        labels = []
        try:
            labels.append(obj.presentation.pk)
        except ObjectDoesNotExist:
            labels.append('?')

        labels.extend([obj.pk, obj.result.status])
        try:
            if obj.presentation.slot:
                labels.append(obj.presentation.slot.day.date)
                labels.append(obj.presentation.slot.start)
                for room in obj.presentation.slot.rooms:
                    labels.append(room.name)
        except ObjectDoesNotExist:
            pass
        labels.extend([obj.speaker.name, unicode(obj)])
        return ", ".join(unicode(l) for l in labels)


class PresentationResourceAdminForm(forms.ModelForm):
    # Adminのフォーム表示をカスタマイズ
    q = ProposalBase.objects.all()
    q = q.exclude(cancelled=True)  # キャンセルプロポーザルは除外
    q = q.order_by(
        'result__status',  # acceptを先に
        'presentation__slot__day__date',  # 日付の早いのを先に
        'presentation__slot__start',  # 時刻の早いのを先に
    )
    proposal_base = PresentationChoideField(queryset=q)

    # 他のフィールドはデフォルト動作でOK

    class Meta:
        model = PresentationResource


class PresentationResourceAdmin(admin.ModelAdmin):
    form = PresentationResourceAdminForm  # Adminのフォーム表示をカスタマイズ

    list_display = [
        'id',
        'proposal_base',
        'type',
        'label',
        'url',
    ]

    class Meta:
        model = PresentationResource

admin.site.register(PresentationResource, PresentationResourceAdmin)
