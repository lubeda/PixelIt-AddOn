from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse,  HttpResponseRedirect
from django.template import loader
from django.db import models
from .models import Screen, Template, Bitmap
from django.conf import settings
from .forms import alarmForm, screenForm, timerForm
from django.utils import timezone
import logging

logger = logging.getLogger(__name__)

# Create your views here.

def screens(request):
    screen_list = Screen.objects.order_by('-start_dt')[:25]

    template = loader.get_template('screens.html')
    context = {
        'now': timezone.now(),
        'screen_list': screen_list,
    }
    return HttpResponse(template.render(context, request))


def index(request):

    template = loader.get_template('index.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


def screen(request, name):
    screen = get_object_or_404(Screen, name=name)
    html_template = loader.get_template('screen.html')
    context = {
        'screen': screen,
    }
    return HttpResponse(html_template.render(context, request))


def templates(request):
    template_list = Template.objects.all()
    html_template = loader.get_template('templates.html')
    context = {
        'template_list': template_list,
    }
    return HttpResponse(html_template.render(context, request))


def template(request, name):
    template = get_object_or_404(Template, name=name)
    html_template = loader.get_template('template.html')
    context = {
        'template': template,
    }
    return HttpResponse(html_template.render(context, request))


def bitmaps(request):
    bmp_list = Bitmap.objects.all
    html_template = loader.get_template('bitmaps.html')
    context = {
        'bmp_list': bmp_list,
        'media_root': settings.MEDIA_ROOT
    }
    return HttpResponse(html_template.render(context, request))

def bitmap(request, name):
    icon = Bitmap.objects.get(name=name)
    logger.info(f"Name ist {name} {icon}")
    html_template = loader.get_template('bitmap.html')
    context = {
        'icon': icon,
    }
    return HttpResponse(html_template.render(context, request))

def screenformview(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = screenForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = screenForm()

    return render(request, 'templateform.html', {'form': form})

def timerformview(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = timerForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            wallo = form.cleaned_data
            screen = Screen()
            screen.name=form.cleaned_data["screen_name"]
            screen.template= Template.objects.get(pk=form.cleaned_data["templates"])
            screen.message=form.cleaned_data["message"]
            screen.start_dt = timezone.now() + form.cleaned_data["delay"]
            screen.end_dt = screen.start_dt + form.cleaned_data["duration"]
            screen.save()
            return HttpResponseRedirect('/gui/screens/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = timerForm()

    return render(request, 'templateform.html', {'form': form})

def alarmformview(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = alarmForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = alarmForm()

    return render(request, 'templateform.html', {'form': form})