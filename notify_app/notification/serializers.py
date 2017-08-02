from rest_framework import serializers
from .models import Notification,Schedule

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ('query','runtime')

class NotificationSerializer(serializers.ModelSerializer):
    schedules = ScheduleSerializer(many=True,source='schedule_set')
    class Meta:
        model = Notification
        fields = ('header','content','image_url','schedules')
