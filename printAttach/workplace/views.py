from django import http, urls
from django.views import generic
from workplace import models

class AbonListView( generic.ListView):
    model = models.Abonent
    template_name = 'abonent_list.html'
    #paginate_by = 5
    #login_url = '/login/'

    def get_queryset(self):
        return models.Abonent.objects.all()



class AbonentCreateView(generic.CreateView):
    model = models.Abonent
    fields = [
        'contract',
        'name',
        'adres',
        'bank',
        'kontact',
        'preabon',
        'pasport'
    ]
    template_name = 'abonent_create.html'
    success_url = urls.reverse_lazy('abonents-list')


class AbonentDetailView(generic.DetailView):
    model = models.Abonent
    template_name = 'abonent_detail.html'

class AbonentUpdateView(generic.UpdateView):
    model = models.Abonent
    fields = [
        'name',
        'adres',
        'bank',
        'kontact',
        'preabon',
        'pasport'
    ]
    template_name = 'abonent_update.html'
    success_url = urls.reverse_lazy('abonents-list')


class AbonentDeleteView(generic.DeleteView):
    model = models.Abonent
    success_url = urls.reverse_lazy('abonents-list')
    template_name = 'abonent_delete.html'

class TarifListView(generic.ListView):
    model = models.Tarif
    template_name = 'tarif_list.html'


    def get_queryset(self):
        return models.Tarif.objects.all()

class TarifCreateView(generic.CreateView):
    model = models.Tarif
    fields = [
        'method',
        'tarif',
        'schet',
        'money',
        'contract'
    ]
    template_name = 'tarif_create.html'
    success_url = urls.reverse_lazy('tarifs-list')

class TarifDetailView(generic.DetailView):
    model = models.Tarif
    template_name = 'tarif_detail.html'

class TarifUpdateView(generic.UpdateView):
    model = models.Tarif
    fields = [
        'method',
        'tarif',
        'schet',
        'money'

    ]
    template_name = 'tarif_update.html'
    success_url = urls.reverse_lazy('tarifs-list')


class TarifDeleteView(generic.DeleteView):
    model = models.Tarif
    success_url = urls.reverse_lazy('tarifs-list')
    template_name = 'tarif_delete.html'

class Index(generic.ListView):
    template_name = 'start_page.html'
