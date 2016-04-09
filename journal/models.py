from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class journalEntry(models.Model):
    user = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    entry = models.TextField(null=False, blank=False)
    sentimentType = models.CharField(max_length=25, null=False, blank=False)
    sentimentScore = models.DecimalField(max_digits=10, decimal_places=6, null=False, blank=False)

    def __unicode__(self):
        return self.entry

class keywords(models.Model):
	entry = models.ForeignKey(journalEntry)
	text = models.CharField(max_length=50, null=False, blank=False)
	relevance = models.DecimalField(max_digits=10, decimal_places=6, null=False, blank=False)
	sentimentType = models.CharField(max_length=25, null=False, blank=False)
	sentimentScore = models.DecimalField(max_digits=10, decimal_places=6, null=False, blank=False)

	def __unicode__(self):
		return self.text

class entities(models.Model):
	entry = models.ForeignKey(journalEntry)
	entityType = models.CharField(max_length=50, null=False, blank=False)
	relevance = models.DecimalField(max_digits=10, decimal_places=6, null=False, blank=False)
	count = models.IntegerField(default=0)
	text = models.CharField(max_length=50, null=False, blank=False)
	sentimentType = models.CharField(max_length=25, null=False, blank=False)
	sentimentScore = models.DecimalField(max_digits=10, decimal_places=6, null=False, blank=False)

	def __unicode__(self):
		return self.text