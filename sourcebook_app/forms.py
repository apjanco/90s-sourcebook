from django import forms
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget
import datetime

from django.db import models
from django.core.files.storage import FileSystemStorage
from sourcebook_app.models import *


class rsvpForm(forms.ModelForm):
	note = forms.CharField(widget=CKEditorWidget(), required=False)
	class Meta:
		fields = ['name','email','note']
		model = rsvp

class SearchForm(forms.Form):
	search = forms.CharField(label='search', max_length=100)