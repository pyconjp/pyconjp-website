from django import forms

from markedit.widgets import MarkEdit
from pycon.models import PyConTalkProposal
from pycon.forms import PyConProposalForm


class PyConJPTalkProposalForm(PyConProposalForm):

    class Meta:
        model = PyConTalkProposal
        fields = [
            "title",
            "category",
            "language",
            "duration",
            "description",
            "audience",
            "audience_level",
            "perceived_value",
            "abstract",
            "outline",
            "additional_notes",
            "additional_requirements",
            "recording_release",
        ]
        widgets = {
            "title": forms.TextInput(attrs={'class': 'fullwidth-input'}),
            "description": forms.Textarea(attrs={'rows': '3'}),
            "audience": forms.TextInput(attrs={'class': 'fullwidth-input'}),
            "perceived_value": forms.Textarea(attrs={'rows': '3'}),
            "abstract": MarkEdit(),
            "outline": MarkEdit(),
            "additional_notes": MarkEdit(attrs={'rows': '3'}),
            "additional_requirements": forms.Textarea(attrs={'rows': '3'}),
        }
