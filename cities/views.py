from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView

from cities.forms import HtmlForm, CityForm
from cities.models import City

__all__ = (
    'home',
    'country1',
    'CityDetailView',
    'CityCreateView',
    'CityUpdateView',
    'CityDeleteView',
    'CityListView',
)

def country1(request, pk=None):

    if request.method == 'POST':
        form1 = CountryForm(request.POST)
        if form1.is_valid():
            print(form1.cleaned_data)
            form1.save()

    form1 = CountryForm()
    ct1 = Country.objects.all()
    context = {'all_country': ct1, 'form1': form1}
    return render(request, 'cities/country.html', context)



def home(request, pk=None):

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()

    form = CityForm()
    qs = City.objects.all()
    lst = Paginator(qs, 2)
    pager_number = request.GET.get('page')
    page_obj = lst.get_page(pager_number)
    context = {'page_obj': page_obj, 'form': form}
    return render(request, 'cities/home.html', context)

class CityDetailView(DetailView):
    queryset = City.objects.all()
    template_name = 'cities/detail.html'



class CityCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = City
    form_class = CityForm
    template_name = 'cities/create.html'
    success_url = reverse_lazy('cities:home')
    success_message = "City created successful"


class CityUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = City
    form_class = CityForm
    template_name = 'cities/update.html'
    success_url = reverse_lazy('cities:home')
    success_message = "City edited successful"


class CityDeleteView(LoginRequiredMixin, DeleteView):
    model = City
#    template_name = 'trains/delete.html'
    success_url = reverse_lazy('cities:home')

    def get(self, request, *args, **kwargs):
        messages.success(request, "City deleted successful")
        return self.post(request, *args, **kwargs)


class CityListView(ListView):
    paginate_by = 5
    model = City
    template_name = 'cities/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = CityForm
        context['form'] = form
        return context
