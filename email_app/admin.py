from django.contrib import admin
from .models import *

@admin.register(EmailTemplate)
class EmailTemplateAdmin(admin.ModelAdmin):
    list_display=['template_type','subject','body']

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display=['name','event_type','date']


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['name','email']



@admin.register(EmailLog)
class EmailLogAdmin(admin.ModelAdmin):
    list_display=['event','employee','status','status','sent_at']


