from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import DetailView, ListView, TemplateView, CreateView, View

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


class DestinationDetailView(DetailView):
    template_name = 'destination_details.html'
    model = TourModel

    # form_class = OrderModelForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context



    def get_success_url(self):
        print(self.request)
        return ""


class PostDestinationDetailView(View):
    def get(self, request, *args, **kwargs):
         view = DestinationDetailView.as_view()
         return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
         view = OrderView.as_view()
         return view(request, *args, **kwargs)
