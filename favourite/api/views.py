from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from favourite.api.paginations import FavouritePagination
from favourite.api.permissions import IsOwner
from favourite.api.serializers import FavouriteAPISerilazer, FavouriteListCreateAPISerilazer
from favourite.models import Favourite
from rest_framework.permissions import IsAuthenticated


class FavouriteListCreateAPIView(ListCreateAPIView):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteListCreateAPISerilazer
    pagination_class = FavouritePagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Favourite.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class FavouriteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteAPISerilazer
    lookup_field = 'pk'
    permission_classes = [IsOwner]
