from django.urls import path
from .views.advertisement_views import AdvertisementListView, AdvertisementDetailView, AdvertisementCreateView, AdvertisementUpdateView, AdvertisementDeleteView
from .views.comments_views import add_comment,delete_comment

app_name = 'webapp'

urlpatterns = [
    path('', AdvertisementListView.as_view(), name='index'),
    path('advertisement/<int:pk>/', AdvertisementDetailView.as_view(), name='advertisement_detail'),
    path('advertisement/create/', AdvertisementCreateView.as_view(), name='advertisement_create'),
    path('advertisement/<int:pk>/update/', AdvertisementUpdateView.as_view(), name='advertisement_update'),
    path('advertisement/<int:pk>/delete/', AdvertisementDeleteView.as_view(), name='advertisement_delete'),
    path('advertisement/<int:advertisement_id>/add_comment/', add_comment, name='add_comment'),
    path('comment/<int:pk>/delete/', delete_comment, name='delete_comment'),
]
