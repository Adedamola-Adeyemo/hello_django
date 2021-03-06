from django.db import models
from django.utils import timezone

class LogMessage(models.Model):
    message = models.CharField(max_length=308)
    log_date = models.DateTimeField("date logged")

    def __str__(self):
        date = timezone.localtime(self.log_date)
        return f"'{self.message}' logged on {date.strftime('%A, %d %B, %Y at %X')}"
# Create your models here
