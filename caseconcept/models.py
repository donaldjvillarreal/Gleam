from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PracticeCal(models.Model):
    # This line is required. Links UserProfile to a User model instance.
	user = models.ForeignKey(User)
	WeekdayTime = models.CharField(max_length=5)

	def __unicode__(self):
		return self.user.username