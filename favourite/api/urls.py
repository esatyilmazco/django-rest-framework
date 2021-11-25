
from favourite.api.views import FavouriteAPIView, FavouriteListCreateAPIView
from django.urls import path

app_name = "favourite"
urlpatterns = [


    path('list-create', FavouriteListCreateAPIView.as_view(), name='list-create'),
    path('update-delete/<pk>', FavouriteAPIView.as_view(), name='update-delete')


]
