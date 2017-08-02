from rest_framework import viewsets,mixins
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from .models import Notification
from .serializers import NotificationSerializer

class NotificationViewSet(
    viewsets.GenericViewSet,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin
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

    def create(self,request,*args,**kwargs):
        #data = request.data
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

        

