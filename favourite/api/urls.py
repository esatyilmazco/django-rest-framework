
from favourite.api.views import FavouriteListCreateAPIView
from django.urls import path

app_name = "favourite"
urlpatterns = [


    path('list-create', FavouriteListCreateAPIView.as_view(), name='list-create')


]
