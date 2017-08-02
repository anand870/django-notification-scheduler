from django.contrib import admin
from .models import Notification,Schedule

class ScheduleInline(admin.StackedInline):
    model = Schedule


class NotificationAdmin(admin.ModelAdmin):
    inlines = [ScheduleInline]


admin.site.register(Notification,NotificationAdmin)
