from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic import TemplateView, CreateView

from pages.forms import ContactModelForm, OrderModelForm
from pages.models import HomeModel, ContactModel, PlaceModel, TripModel
from django.contrib import messages


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


# class ContactView(CreateView):
#     template_name = 'contact.html'
#     form_class = ContactModelForm
#
#     def get_success_url(self):
#         return reverse('pages:contact')


def contact(request):
    form = ContactModelForm
    if request.method == "POST":
        form = ContactModelForm(request.POST)
        # messages.add_message(request, messages.INFO, 'uhjsdhsjdhjshd')
        if form.is_valid():
            form.save()
            messages.info(request, 'Отправлено')
            return redirect('pages:contact')
    return render(request, "contact.html")


class AboutView(TemplateView):
    template_name = 'about.html'


class LoginView(TemplateView):
    template_name = 'login.html'


class RegisterView(TemplateView):
    template_name = 'register.html'


class OrderView(CreateView):
    template_name = 'orders.html'
    form_class = OrderModelForm

    def get_success_url(self):
        return reverse('pages:order')


def order(request):
    form = OrderModelForm()
    if request.method == "POST":
        form = OrderModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Отправлено')
    return render(request, "orders.html")

#
# class InputView(TemplateView):
#     template_name = 'input.html.'
