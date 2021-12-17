from django.shortcuts import render
from django.urls import reverse
from django.views.generic import DetailView, ListView, TemplateView, CreateView

from tours.forms import OrderModelForm
from tours.models import TourTagModel, TourModel


class DestinationsListView(ListView):
    template_name = 'destinations.html'

    def get_queryset(self):
        qs = TourModel.objects.order_by('-pk')

        q = self.request.GET.get('q')

        if q:
            qs = qs.filter(title__icontains=q)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brands'] = TourTagModel.objects.order_by('-pk')
        context['brands'] = TourTagModel.objects.order_by('-pk')
        return context


class InputListView(ListView):
    template_name = 'input.html'

    def get_queryset(self):
        qs = TourModel.objects.order_by('-pk')

        q = self.request.GET.get('q')

        if q:
            qs = qs.filter(title__icontains=q)
        return qs


class DestinationCreateView(DetailView):
    template_name = 'destination_details.html'
    model = TourModel
    # form_class = OrderModelForm

    def get_context_data(self, pk, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related'] = TourModel.objects.filter(id=pk)
        return context
