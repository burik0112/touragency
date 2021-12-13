from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import TemplateView, CreateView

from pages.forms import ContactModelForm
from pages.models import HomeModel, ContactModel, PlaceModel, TripModel


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_queryset(self):
        qs = HomeModel.object.order_by('-pk')

        q = self.request.GET.get('q')

        if q:
            qs = qs.filter(title__icontains=q)

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['homes'] = HomeModel.objects.order_by('-pk')
        context['contacts'] = ContactModel.objects.order_by('-pk')
        context['places'] = PlaceModel.objects.order_by('-pk')
        context['trips'] = TripModel.objects.order_by('-pk')
        return context


class ContactView(CreateView):
    template_name = 'contact.html'
    form_class = ContactModelForm

    def get_success_url(self):
        return reverse('pages:contact')


class AboutView(TemplateView):
    template_name = 'about.html'


class LoginView(TemplateView):
    template_name = 'login.html.'
#
#
# class InputView(TemplateView):
#     template_name = 'input.html.'




