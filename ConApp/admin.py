from django.contrib import admin
from ConApp.models import SamedNotes, MamadouNotes

from import_export.admin import ImportExportModelAdmin

# Register your models here.
admin.site.register(SamedNotes)
admin.site.register(MamadouNotes)



class MamadouNotesAdmin(ImportExportModelAdmin):
        #list_display = ('day', 'notes',)
        pass

admin.site.register(MamadouNotes, AdminNotes)
