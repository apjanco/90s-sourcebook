from django.db import models
from ckeditor.fields import RichTextField
#
# Create your models here.

class rsvp(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    note = RichTextField(blank=True)

    def __str__(self):
       return self.name

class item(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    category = models.ManyToManyField('category', blank=True)
    #subcategory = models.ManyToManyField('subcategory', blank=True)
    source = models.CharField(max_length=200, blank=True, null=True)
    url = models.URLField(max_length=200, blank=True, null=True)
    file = models.FileField(upload_to='media/')
    essay = RichTextField(blank=True)

    def __str__(self):
        return self.title

class category(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    essay = RichTextField(blank=True)
    def __str__(self):
        return self.title


