from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse, reverse_lazy
from .models import World


class WorldListView(ListView):
    model = World
    template_name = 'helloworld/world_list.html'
    context_object_name = 'worlds'


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
