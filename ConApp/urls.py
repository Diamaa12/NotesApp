
from django.contrib import admin
from django.urls import path
from .views import subcription,  mamadou_notes, samed_notes, user_login, logout_view, mamadou_items_del, samed_items_del
#from .test import export_data

urlpatterns = [
    #path('Import/', export_data, name='exportation'),
    path('admin-ley/', admin.site.urls),
    path('subcription/', subcription, name='to-subcribe'),
    path('login/', user_login, name='login-user'),
    path('logout/', logout_view, name='logout-user'),
    path('mamadou/', mamadou_notes, name="mamadou-notice"),
    path('mamadou/<int:id>', mamadou_items_del, name="mamadou_items_del"),
    path('samed/', samed_notes, name='samed-notice'),
    path('samed/<int:id>', samed_items_del, name="samed_items_del"),
    ]