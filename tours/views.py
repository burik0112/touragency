from django.shortcuts import render
from django.views.generic import DetailView, ListView


class DestinationListView(ListView):
    templates_name = 'travel_destination.html'


class DestinationDetailView(DetailView):
    templates_name = 'destination_details.html'
