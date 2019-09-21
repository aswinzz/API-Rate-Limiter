from django.db import models
from django.contrib.auth.models import User

class RateLimits(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    url=models.TextField(null=False,blank=False)
    count=models.IntegerField(default=0)
    lastupdated=models.DateTimeField(auto_now_add=True, blank=True)
    maxrate=models.IntegerField(default=10)
    
    def __unicode__(self):
        return self.user