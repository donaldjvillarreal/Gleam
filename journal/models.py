from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class journalEntry(models.Model):
    user = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    entry = models.TextField(null=False, blank=False)
    sentimentType = models.CharField(max_length=25, null=False, blank=False)
    sentimentScore = models.DecimalField(max_digits=10, decimal_places=4, null=False, blank=False)

    def __unicode__(self):
        return self.entry