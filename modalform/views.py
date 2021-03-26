from django.views.generic.detail import DetailView
from bootstrap_modal_forms.generic import BSModalUpdateView
from django.urls import reverse_lazy
from .models import Post
from .forms import PostCategoryForm


class PostDetailView(DetailView):
    template_name = 'post.html'
    model = Post
    context_object_name = 'post'


class PostCategoryView(BSModalUpdateView):
    template_name = '_modal_select2_form.html'
    form_class = PostCategoryForm
    model = Post
    
    def get_success_url(self):
        return reverse_lazy('post', kwargs={'pk': self.kwargs.get('pk')})

    def get_context_data(self, *args, **kwargs):
        context = super(PostCategoryView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Select Category'
        return context
    