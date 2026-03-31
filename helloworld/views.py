from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy
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


def send_hello(request, pk):
    world = get_object_or_404(World, pk=pk)
    if request.method == 'POST':
        world.send_hello()
    return redirect('helloworld:world_detail', pk=pk)
