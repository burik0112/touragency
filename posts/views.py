from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import DetailView, ListView, CreateView

from posts.forms import CommentModelForm
from posts.models import PostModel


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
    template_name = 'blog-detail.html'
    model = PostModel


class CommentCreateView(CreateView):
    forms_class = CommentModelForm

    def form_valid(self, form):
        form.instance.post = get_object_or_404(PostModel, pk=self.kwargs['pk'])
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post:detail', kwargs={'pk': self.kwargs['pk']})
