from django.forms import ModelForm
from .models import WorkingHours

class WorkingHoursForm(ModelForm):
    class Meta:
        model = WorkingHours
        fields = '__all__'