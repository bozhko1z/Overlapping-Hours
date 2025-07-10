from django import forms
from django.forms import modelformset_factory
from overlap_app.models import WorkingHours


class WorkingHoursForm(forms.ModelForm):
    class Meta:
        model = WorkingHours
        fields = ["day", "start", "end"]
