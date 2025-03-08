from django.db import models

# Create your models here.

class Summary(models.Model):
	url = models.CharField(max_length=255)
	title = models.CharField(max_length=255, unique=True)
	content = models.TextField(blank=True)
	slug = models.SlugField(max_length=255)
	created = models.DateTimeField(auto_now_add=True, null=True) # only trigger once

	class Meta:
		verbose_name_plural = "Summaries"
		ordering = ("-created", ) # The sign means descengin order

	def __str__(self):
		return self.title
