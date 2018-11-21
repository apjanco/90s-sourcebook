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


class KO(models.Model):

    file = models.FileField(blank=True, null=True)
    filename = models.CharField(max_length=200, blank=True, null=True)
    journal = models.CharField(max_length=200, blank=True, null=True)
    year = models.CharField(max_length=200, blank=True, null=True)
    issue = models.CharField(max_length=200, blank=True, null=True)
    date = models.CharField(max_length=200, blank=True, null=True)
    text = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.filename


class BestsellerList(models.Model):
    journal = models.CharField(max_length=200, blank=True, null=True)
    year = models.CharField(max_length=200, blank=True, null=True)
    issue = models.CharField(max_length=200, blank=True, null=True)
    date = models.CharField(max_length=200, blank=True, null=True)
    category = models.CharField(max_length=200, blank=True, null=True)
    rank = models.CharField(max_length=200, blank=True, null=True)
    author = models.CharField(max_length=200, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    place = models.CharField(max_length=200, blank=True, null=True)
    publisher = models.CharField(max_length=200, blank=True, null=True)
    russian = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return '{}-{}-{}-{}'.format(self.journal, self.year, self.issue, self.rank)


class category(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    essay = RichTextField(blank=True)
    def __str__(self):
        return self.title


