from django.urls import path

from .views.advertisement_views import HomeView
from .views.advertisement_views import AdvertisementListView, AdvertisementDetailView, AdvertisementCreateView, AdvertisementUpdateView, AdvertisementDeleteView



app_name = 'webapp'

urlpatterns = [
    # path('', HomeView.as_view(), name='index'),
    # path('advertisements/', AdvertisementListView.as_view(), name='advertisement_list'),
    path('', AdvertisementListView.as_view(), name='index'),
    path('advertisement/<int:pk>/', AdvertisementDetailView.as_view(), name='advertisement_detail'),
    path('advertisement/create/', AdvertisementCreateView.as_view(), name='advertisement_create'),
    path('advertisement/<int:pk>/update/', AdvertisementUpdateView.as_view(), name='advertisement_update'),
    path('advertisement/<int:pk>/delete/', AdvertisementDeleteView.as_view(), name='advertisement_delete'),

]