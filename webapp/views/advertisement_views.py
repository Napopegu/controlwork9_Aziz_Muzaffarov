from django.shortcuts import  redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from webapp.models import Advertisement
from webapp.forms import AdvertisementForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse




class HomeView(TemplateView):
    template_name = 'index.html'


class AdvertisementListView(ListView):
    model = Advertisement
    template_name = 'advertisements/advertisement_list.html'
    context_object_name = 'advertisements'
    queryset = Advertisement.objects.filter(status_choices='published').order_by('-published_at')

class AdvertisementDetailView(DetailView):
    model = Advertisement
    template_name = 'advertisements/advertisement_detail.html'


class AdvertisementCreateView(LoginRequiredMixin, CreateView):
    model = Advertisement
    form_class = AdvertisementForm
    template_name = 'advertisements/advertisement_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:index')


class AdvertisementUpdateView(UpdateView):
    model = Advertisement
    form_class = AdvertisementForm
    template_name = 'advertisements/advertisement_update.html'

    def get_success_url(self):
        return reverse('webapp:index')

class AdvertisementDeleteView(DeleteView):
    model = Advertisement
    template_name = 'advertisements/advertisement_delete.html'

    def get_success_url(self):
        return reverse('webapp:index')


    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.status = 'deleted'
        self.object.save()
        return redirect(self.get_success_url())





