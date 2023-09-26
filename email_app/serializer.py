# event_email_app/serializers.py
from rest_framework import serializers
from .models import Event, EmailTemplate, Employee, EmailLog

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields='__all__'

