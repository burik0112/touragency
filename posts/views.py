from urllib import request
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.views.generic import DetailView, ListView, CreateView, View
from posts.forms import CommentModelForm
from posts.models import PostModel, CommentModel


class PostListView(ListView):
    template_name = 'blog.html'
    paginate_by = 3

    def get_queryset(self):
        qs = PostModel.objects.order_by("-pk")

        tag = self.request.GET.get('tag')

        if tag:
            qs = qs.filter(tags__title=tag)

        return qs


class PostDetailView(DetailView):
    template_name = 'blog_detail.html'
    model = PostModel


def add_comment():
    comment = []

    if messages == comment['pk']:
        messages.add_message(request, messages.INFO, 'Product removed from cart')
    else:
        messages.add_message(request, messages.INFO, 'Product added to cart')
    # if pk in cart:
    #     messages.add_message(request, messages.INFO, 'Product removed from cart')
    # else:
    #     messages.add_message(request, messages.INFO, 'Product added to cart')


class CommentCreateView(SuccessMessageMixin, CreateView):
    model = CommentModel
    form_class = CommentModelForm

    def form_valid(self, form):
        form.instance.post = get_object_or_404(PostModel, pk=self.kwargs['pk'])
        form.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('posts:detail', kwargs={'pk': self.kwargs['pk']})

def order(request):
    form = CommentModelForm()
    if request.method == "POST":
        form = CommentModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'comment sent')
    return render(request, "blog_details.html")

# class CommentCreateView(View):
#     def post(self, request, pk):
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         email = request.POST.get('email')
#         comment = request.POST.get('comment')
#         done = CommentModel.objects.create(post_id=pk, name=name, phone=phone, email=email, comment=comment)
#         return render(request, 'blog_detail.html', pk=pk)
