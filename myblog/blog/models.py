from django.db import models
from django.utils import timezone


# Create your models here.
class blog_post(models.Model):
	author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
	title = models.CharField(max_length = 100)
	description = models.TextField()
	created_date = models.DateTimeField(default = timezone.now)
	published_date = models.DateTimeField(blank = None, null = True)

	def publish(self):
		self.published_date = timezone.now
		self.save()

	def __str__(self):
		return self.title