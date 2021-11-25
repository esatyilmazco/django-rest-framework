

from rest_framework.generics import ListCreateAPIView
from favourite.api.serializers import FavouriteListCreateAPISerilazer
from favourite.models import Favourite


class FavouriteListCreateAPIView(ListCreateAPIView):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteListCreateAPISerilazer

    def get_queryset(self):
        return Favourite.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
