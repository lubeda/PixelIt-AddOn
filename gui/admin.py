from django.contrib import admin
from .models import Screen, Template
from django.contrib.postgres.fields import JSONField
from jsoneditor.forms import JSONEditor
from django.db import models


@admin.register(Screen)
class ScreenAdmin(admin.ModelAdmin):
    pass


@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):
    pass
