from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.urls import reverse

class Book(models.Model):
	TYPE_CHOICES = (
			('Journal', 'Journal'),
			('Conference', 'Conference'),
			('Book', 'Book'),
			('Other', 'Other'),
			)
	author1 = models.CharField(max_length=100)
	author2 = models.CharField(max_length=1000) # other authors sep=','
	a_title = models.CharField(max_length=250)
	a_type = models.CharField(max_length=10,
							choices=TYPE_CHOICES, default='journal')
	uploaded = models.DateTimeField(auto_now_add=True)
	uploader = models.CharField(max_length=100)
	pdf_file = models.FileField(upload_to='static/media')



	def __str__(self):
		return self.a_title


# model for the items held in the library
class Holdings(models.Model):
    TYPE_CHOICES = (
			('journal', 'Journal'),
			('conference', 'Conference'),
			('book', 'Book'),
			('other', 'Other'),
			)
    title = models.CharField(max_length=255)
    holding = models.FileField(upload_to='static/media')
    uploaded = models.DateTimeField(auto_now_add=True)
    authors = models.CharField(max_length=100)
    category = models.CharField(max_length=10,
							choices=TYPE_CHOICES, default='journal')
    uploader = models.CharField(max_length=100)

    objects = models.Manager()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
    	return reverse('app_name:download', args=[str(self.holding)])