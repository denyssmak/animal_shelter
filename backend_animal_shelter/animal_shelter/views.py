import pdfkit as pdfkit
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template.loader import get_template
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView

from animal_shelter.forms import (
    CreateAnimalDataForm,
    UpdateAnimalDataForm,
    AnimalTypeFilterForm,
    AnimalReasonForDeletionForm,
    MedicalCardCreateDiseaseForm,
)
from animal_shelter.models import (
    Animal,
    AnimalDeleteLog,
    MedicalCard,
)


class AnimalListView(ListView):
    model = Animal
    template_name = 'index.html'
    extra_context = {'filter': AnimalTypeFilterForm}

    def get_queryset(self):
        if self.request.GET.get('animal_filter'):
            return self.model.objects.filter(
                animal_type=self.request.GET['animal_filter'],
                deleted=False
            )

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
        AnimalDeleteLog.objects.create(
            animal=animal,
            reason=form.data['reason']
        )
        return super().form_valid(form=form)


class MedicalCardCreateDiseaseView(CreateView):
    model = MedicalCard
    template_name = 'create_disease.html'
    form_class = MedicalCardCreateDiseaseForm

    def form_valid(self, form):
        object = form.save(commit=False)
        pk = self.kwargs['pk']
        animal = get_object_or_404(Animal, id=pk)
        object.animal = animal
        object.save()
        return super().form_valid(form=form)

    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        self.object = None
        context = self.get_context_data()
        context['animal_diseases'] = Animal.objects.get(
            id=pk
        ).animal_diseases.all()
        return self.render_to_response(context)

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse('create_disease', kwargs={'pk': pk})


class GenerateAnimalPDF(View):
    model = Animal
    template_name = 'animal_pdf.html'

    def post(self, request, *args, **kwargs):
        options = {}
        pk = kwargs['pk']
        animal = get_object_or_404(Animal, id=pk)
        data = {
            'name':animal.name,
            'date': animal.date,
            'height': animal.height,
            'weight': animal.weight,
            'passport': animal.passport,
        }

        template = get_template('animal_pdf.html')
        path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
        config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
        template_data = template.render(context=data)
        print(template_data)
        # wkhtmltopdf_cmd = subprocess.Popen(['which', os.environ.get('WKHTMLTOPDF_BINARY', 'wkhtmltopdf-pack')],
        #                                    stdout=subprocess.PIPE).communicate()[0].strip()
        # configuration = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_cmd)
        pdf_file = pdfkit.from_string(template_data, False, options, configuration=config)
        response = HttpResponse(pdf_file, content_type='application/pdf')
        response['Content-Disposition'] = "attachment; filename=%s" % 'animal_' + animal.name + '.pdf'
        print(response['Content-Disposition'])

        return response


