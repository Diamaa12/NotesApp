from import_export import resources
from .models import MamadouNotes

class AdminMamadouNotes(resources.ModelResource):
    class Meta:
        model = MamadouNotes