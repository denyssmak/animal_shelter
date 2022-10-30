from django.shortcuts import render
from .models import Animal, AnimalDeleteLog, MedicalСard
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .forms import CreateAnimalDataForm, UpdateAnimalDataForm, AnimalTypeFilterForm, AnimalReasonForDeletionForm, MedicalСardCreateDiseaseForm




class AnimalListView(ListView):
    model = Animal
    template_name = 'index.html'
    extra_context = {'filter': AnimalTypeFilterForm}  


    def get_queryset(self):
        if self.request.GET.get('animal_filter'):
            return self.model.objects.filter(animal_type=self.request.GET['animal_filter'], deleted=False)

        return self.model.objects.filter(deleted=False)


class CreateAnimalDataView(CreateView):
    template_name = 'create_animal_data.html'
    form_class = CreateAnimalDataForm
    success_url = reverse_lazy('index')
    
 

class UpdateAnimalDataView(UpdateView):
    model = Animal
    template_name = 'update_animal_data.html'
    form_class = UpdateAnimalDataForm
    success_url = reverse_lazy('index')



class DeleteAnimalDataView(UpdateView):
    model = Animal
    template_name = 'delete_animal_data.html'
    form_class = AnimalReasonForDeletionForm
    success_url = reverse_lazy('index')


    def form_valid(self, form):
        animal = form.save(commit=False)
        animal.deleted = True
        AnimalDeleteLog.objects.create(animal=animal, reason=form.data['reason'])
        return super().form_valid(form=form)


class MedicalСardCreateDiseaseView(CreateView):
    model = MedicalСard
    template_name = 'create_disease.html'
    form_class = MedicalСardCreateDiseaseForm
    

    def form_valid(self, form):
        object = form.save(commit=False)
        pk = self.kwargs['pk']
        animal = Animal.objects.get(id=pk)
        object.animal = animal
        object.save()
        return super().form_valid(form=form)


    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        print(kwargs, args)
        self.object = None
        context = self.get_context_data()
        context['animal_diseases'] = Animal.objects.get(id=pk).animal_diseases.all()
        return self.render_to_response(context)


    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse('create_disease', kwargs={'pk': pk})