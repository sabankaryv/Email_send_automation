from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.core.management.base import BaseCommand
from django.core.mail import send_mail ,BadHeaderError
from django.conf import settings
from .models import *
from datetime import date
from django.conf import settings
from validate_email import validate_email
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import EmployeeSerializer


@api_view(['GET','POST'])
def get_event(request):
    if request.method=="GET":
        today = date.today()
        events_today = Event.objects.filter(date=today).values('date','name')
        for event in events_today:
            event_name=event['name']
            event_today=event['date']
            if not events_today:
                return
            events_template = EmailTemplate.objects.filter(template_type=event_name)
            for event_data in events_template:
                event_name=event_data.template_type
                event_body=event_data.body
                event_subject=event_data.subject
                employees = Employee.objects.all()
                for employee in employees: 
                    email_template = EmailTemplate.objects.get(template_type=event_name)
                    subject = f'Event Reminder: {event_name}'
                    from_email =settings.EMAIL_HOST_USER
                    recipient_list = [employee.email]
                    email_body = email_template.body.replace('{{ employee_name }}', employee.name)
                    email_body = email_body.replace('{{ event_name }}',event_name)
                    try:
                        data=send_mail(subject, email_body, from_email, recipient_list, fail_silently=True)
                    except BadHeaderError as e:
                        print("")
        return Response({"message": "Emails sent successfully."})
    if request.method=="POST":
        serializer_object=EmployeeSerializer(data=request.data)
        if serializer_object.is_valid():
            serializer_object.save()
            return Response({"msg":"Data Added Successfully.....!"})
        return Response(serializer_object.errors)