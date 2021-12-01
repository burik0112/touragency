from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import TemplateView, CreateView

from pages.forms import ContactModelForm
from pages.models import HomeModel, ContactModel, PlaceModel


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['homes'] = HomeModel.objects.order_by('-pk')
        context['contacts'] = ContactModel.objects.order_by('-pk')
        context['place'] = PlaceModel.objects.order_by('-pk')
        return context


class ContactView(CreateView):
    template_name = 'contact.html'
    form_class = ContactModelForm

    def get_success_url(self):
        return reverse('pages:contact')


class AboutView(TemplateView):
    template_name = 'about.html'



