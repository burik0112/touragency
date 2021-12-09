from django.shortcuts import render
from django.views.generic import DetailView, ListView

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


class DestinationDetailView(DetailView):
    templates_name = 'destination_details.html'
