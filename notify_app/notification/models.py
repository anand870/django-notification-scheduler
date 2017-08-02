from django.db import models

class Notification(models.Model):
    header = models.CharField(max_length=150)
    content = models.CharField(max_length=300)
    image_url = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.header


class Schedule(models.Model):
    """
    Model to hold the state of a scheduled notification.Each notification
    may have multiple scheduling time with different target users.
    """
    runtime = models.DateTimeField()
    query = models.CharField(max_length = 500)
    #task_id holds the celery task id to cancel a already scheduled task
    task_id = models.CharField(max_length=50, blank=True, editable=False)
    notification = models.ForeignKey(Notification,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
