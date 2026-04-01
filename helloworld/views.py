from django.forms import modelform_factory
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.edit import FormMixin
from django.urls import reverse, reverse_lazy
from .models import World


class WorldListView(FormMixin, ListView):
    model = World
    template_name = 'helloworld/world_list.html'
    context_object_name = 'worlds'
    success_url = reverse_lazy('helloworld:world_list')

    def get_form_class(self):
        return modelform_factory(World, fields=['name'])

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        self.object_list = self.get_queryset()
        return self.render_to_response(self.get_context_data(form=form))

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class WorldDetailView(DetailView):
    model = World
    template_name = 'helloworld/world_detail.html'
    context_object_name = 'world'


class WorldCreateView(CreateView):
    model = World
    template_name = 'helloworld/world_form.html'
    fields = ['name']
    success_url = reverse_lazy('helloworld:world_list')


@require_POST
def send_hello(request, pk):
    world = get_object_or_404(World, pk=pk)
    world.send_hello()
    return redirect(reverse('helloworld:world_detail', args=[pk]) + '?greeted=1')
