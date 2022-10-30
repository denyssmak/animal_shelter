from django.contrib import admin
from animal_shelter.views import AnimalListView, CreateAnimalDataView, UpdateAnimalDataView, DeleteAnimalDataView, MedicalСardCreateDiseaseView
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', AnimalListView.as_view(), name='index'),
    path('create_aminal_data/', CreateAnimalDataView.as_view(), name='create_aminal_data'),
    path('update_aminal_data/<int:pk>/', UpdateAnimalDataView.as_view(), name='update_aminal_data'),
    path('delete_aminal_data/<int:pk>/', DeleteAnimalDataView.as_view(), name='delete_aminal_data'),
    path('create_disease/<int:pk>/', MedicalСardCreateDiseaseView.as_view(), name='create_disease')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)