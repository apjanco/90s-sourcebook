from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class rsvp(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    note = RichTextField(blank=True)

    def __str__(self):
       return self.name
