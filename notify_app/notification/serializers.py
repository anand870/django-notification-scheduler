from rest_framework import serializers
from .models import Notification,Schedule

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ('query','runtime','id')

    def validate(self,attrs):
        # @TODO: Validate that the time is in future
        #@TODO : Validate that the query is proper
        return attrs

class NotificationSerializer(serializers.ModelSerializer):
    schedules = ScheduleSerializer(many=True,source='schedule_set',required=False)
    class Meta:
        model = Notification
        fields = ('id','header','content','image_url','schedules')

    def save(self):
        import pdb;pdb.set_trace()
        validated_data = self.validated_data
        #remove the set of schedules
        schedules = validated_data.pop('schedule_set')
        #save notifications models
        if self.instance is not None:
            self.instance = self.update(self.instance,validated_data)
        else:
            self.instance = self.create(validated_data)
        #add schedules
        self.instance.create_or_update_schedule(schedules)
        return self.instance


