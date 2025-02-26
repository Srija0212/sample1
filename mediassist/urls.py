from django.contrib import admin
from django.urls import path
from prescriptions.views import home, process_prescription  # Import home view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),  # Add this line for the home page
    path("process/", process_prescription, name="process_prescription"),
    

]

from django.urls import path


urlpatterns = [
    path('', home, name='home'),
    path('process/', process_prescription, name='process_prescription'),
]
from django.contrib import admin
from django.urls import path
from prescriptions.views import home, process_prescription  # Import home view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),  # Add this line for the home page
    path("process/", process_prescription, name="process_prescription"),
    

]

from django.urls import path


urlpatterns = [
    path('', home, name='home'),
    path('process/', process_prescription, name='process_prescription'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('patients/', views.patient_list, name='patient_list'),
    path('patients/add/', views.add_patient, name='add_patient'),
    path('patients/delete/<int:id>/', views.delete_patient, name='delete_patient'),
]
