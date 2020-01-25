from django import forms
from .models import Screen, Template, Bitmap
from django.utils import timezone
from durationwidget.widgets import TimeDurationWidget
# https://pypi.org/project/django-durationwidget/
import datetime

class DateTimeInput(forms.DateTimeInput):
    input_type = "datetime-local"

    def __init__(self, **kwargs):
        kwargs["format"] = "%Y-%m-%dT%H:%M"
        super().__init__(**kwargs)


class screenForm(forms.Form):
    screen = forms.CharField(label='Screen name', max_length=10)
    message = forms.CharField(label='Display text:', max_length=20)
    duration = forms.DurationField(label='Display duration:', initial="00:05:00", widget=TimeDurationWidget(show_days=False, show_hours=True, show_minutes=True, show_seconds=False))
    templates = forms.ChoiceField(choices = [(templ.pk, templ.name) for templ in Template.objects.all()],label="Template")

class timerForm(forms.Form):
    screen_name = forms.CharField(label='Screen name', max_length=10)
    duration = forms.DurationField(label='Display duration:', initial="00:05:00", widget=TimeDurationWidget(show_days=False, show_hours=True, show_minutes=True, show_seconds=False))
    delay = forms.DurationField(label='Show in... (/delay)', initial="00:00:00", widget=TimeDurationWidget(show_days=False, show_hours=True, show_minutes=True, show_seconds=False))
    message = forms.CharField(label='Display text:', max_length=20)
    templates = forms.ChoiceField(choices=[(templ.pk, templ.name) for templ in Template.objects.all()],
                                  label="Template")

class alarmForm(forms.Form):
    screen_name = forms.CharField(label='Your name', max_length=10)
    duration = forms.DurationField(label='Display duration:', initial="00:05:00", widget=TimeDurationWidget(show_days=False, show_hours=True, show_minutes=True, show_seconds=False))
    start_at = forms.DateTimeField(label="Start date",initial=timezone.now(),widget=DateTimeInput)
    message = forms.CharField(label='Display text:', max_length=20,)
    templates = forms.ChoiceField(choices=[(templ.pk, templ.name) for templ in Template.objects.all()],
                                 label="Template")

