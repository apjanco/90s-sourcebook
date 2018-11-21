from django.contrib import admin
from sourcebook_app.models import *
from django.contrib.flatpages.models import FlatPage

# Note: we are renaming the original Admin and Form as we import them!
from django.contrib.flatpages.admin import FlatPageAdmin as FlatPageAdminOld
from django.contrib.flatpages.admin import FlatpageForm as FlatpageFormOld

from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
# Register your models here.

from django import forms

class FlatpageForm(FlatpageFormOld):
  content = forms.CharField(widget=CKEditorUploadingWidget())
  class Meta:
    model = FlatPage # this is not automatically inherited from FlatpageFormOld
    fields = '__all__'

class FlatPageAdmin(FlatPageAdminOld):
  form = FlatpageForm

#We have to unregister the normal admin, and then reregister ours
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)

class rsvpAdmin(admin.ModelAdmin):
    pass

admin.site.register(rsvp, rsvpAdmin)

class itemAdmin(admin.ModelAdmin):
    pass

admin.site.register(item, itemAdmin)

class KOAdmin(admin.ModelAdmin):
    search_fields = ['filename', 'text', ]
    list_display = ['filename', 'year', 'issue', 'date',]
    list_filter = ['year', 'issue', ]

admin.site.register(KO, KOAdmin)

class categoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(category, categoryAdmin)

#class subcategoryAdmin(admin.ModelAdmin):
#    pass

#admin.site.register(subcategory, subcategoryAdmin)
class BestsellerListAdmin(admin.ModelAdmin):
    search_fields = ['author', 'title', ]
    list_display = ['author', 'title', 'journal', 'year', 'issue', 'date', 'rank', ]
    list_filter = ['year', 'issue', 'date', 'rank', ]

admin.site.register(BestsellerList, BestsellerListAdmin)

