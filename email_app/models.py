# event_email_app/models.py
from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=255)
    event_type = models.CharField(max_length=255)
    date = models.DateField()

class EmailTemplate(models.Model):
    template_type = models.CharField(max_length=255, unique=True)
    subject = models.CharField(max_length=255)
    body = models.TextField()

class Employee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

class EmailLog(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    status = models.CharField(max_length=255)
    error_message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
