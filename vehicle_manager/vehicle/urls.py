from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

app_name = 'vehicle'

urlpatterns = [
    path('',views.index,name='index'),
    path('download_vehicle_pdf/<int:vehicle_id>/',views.download_vehicle_pdf,name='download_vehicle_pdf'),

    # Login and logout
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
]