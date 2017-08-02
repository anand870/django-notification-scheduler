from rest_framework import viewsets,mixins
from rest_framework.response import Response

from .models import Notification
from .serializers import NotificationSerializer

class NotificationViewSet(
    viewsets.GenericViewSet,
    mixins.RetrieveModelMixin
):
    queryset = Notification.objects
    serializer_class = NotificationSerializer

    def get_queryset(self):
        if self.action == 'list':
            return self.queryset.prefetch_related('schedule_set')
        return self.queryset

    def list(self,request,*args,**kwargs):
        """
        Notification Listing view.Fetches all the notifications.
        @TODO : implement pagination
        """
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset,many=True)
        return Response(serializer.data)
        

