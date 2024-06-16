from django.urls import path
from . import views

app_name = 'vehicle'

urlpatterns = [
    path('',views.index,name='index'),
    path('download_vehicle_pdf/<int:vehicle_id>/',views.download_vehicle_pdf,name='download_vehicle_pdf'),
]