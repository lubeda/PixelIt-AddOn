from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Screen, Template


# Create your views here.

def screens(request):
    screen_list = Screen.objects.order_by('-start_dt')[:5]

    template = loader.get_template('screens.html')
    context = {
        'screen_list': screen_list,
    }
    return HttpResponse(template.render(context, request))


def screen(request, name):
    screen_list = get_object_or_404(Screen, name=name)
    html_template = loader.get_template('screens.html')
    context = {
        'screen_list': screen_list,
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
    screen_list = Screen.objects.get(name=name)
    template = loader.get_template('screens.html')
    context = {
        'screen_list': screen_list,
    }
    return HttpResponse(template.render(context, request))
