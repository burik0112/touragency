from django.shortcuts import render
from django.views.generic import DetailView, ListView

from tours.models import TourTagModel, TourModel


class DestinationsListView(ListView):
    template_name = 'destinations.html'
    paginate_by = 3

    def get_queryset(self):
        qs = TourModel.objects.order_by('-pk')

        q = self.request.GET.get('q')
        cat = self.request.GET.get('cat')
        tag = self.request.GET.get('tag')
        sort = self.request.GET.get('sort')
        price = self.request.GET.get('price')


        if q:
            qs = qs.filter(title__icontains=q)

        if cat:
            qs = qs.filter(category_id=cat)

        if tag:
            qs = qs.filter(tags__id=tag)

        if price:
            price_from, price_to = price.split(';')
            qs = qs.filter(real_price__gte=price_from, real_price__lte=price_to)

        if sort:
            if sort == 'price':
                qs = qs.order_by('real_price')
            elif sort == '-price':
                qs = qs.order_by('-real_price')
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brands'] = TourTagModel.objects.order_by('-pk')
        return context


class DestinationDetailView(DetailView):
    templates_name = 'destination_details.html'
