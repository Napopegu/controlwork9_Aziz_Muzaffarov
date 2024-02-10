from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, View, TemplateView




class HomeView(TemplateView):
    template_name = 'index.html'
    # context_object_name = 'publications'