from django.contrib import admin
from django.urls import include, path

from hospital import views


urlpatterns = [

    path('admin/', admin.site.urls),

    # REST API
    path('api/', include('hospital.urls')),

    # Website pages
    path('', views.home, name='home'),

    path('patients/', views.patients_page, name='patients'),

    path('doctors/', views.doctors_page, name='doctors'),

    path('appointments/', views.appointments_page, name='appointments'),

    path('treatments/', views.treatments_page, name='treatments'),
]