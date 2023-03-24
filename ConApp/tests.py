from django.http import HttpResponse

from .ressources import AdminMamadouNotes

def export_data(request):
    dataset = AdminMamadouNotes().export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="mymodel.csv"'
    return response

# Create your tests here.
