from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from animal_shelter.views import (
    AnimalListView,
    CreateAnimalDataView,
    UpdateAnimalDataView,
    DeleteAnimalDataView,
    MedicalCardCreateDiseaseView,
)

urlpatterns = [
    path('', AnimalListView.as_view(), name='index'),
    path('create_animal_data/', CreateAnimalDataView.as_view(), name='create_animal_data'),
    path('update_animal_data/<int:pk>/', UpdateAnimalDataView.as_view(), name='update_animal_data'),
    path('delete_animal_data/<int:pk>/', DeleteAnimalDataView.as_view(), name='delete_animal_data'),
    path('create_disease/<int:pk>/', MedicalCardCreateDiseaseView.as_view(), name='create_disease')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
