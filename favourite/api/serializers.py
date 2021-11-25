

from rest_framework.serializers import ModelSerializer
from favourite.models import Favourite
from django.contrib.sessions import serializers


class FavouriteListCreateAPISerilazer(ModelSerializer):
    class Meta:
        model = Favourite
        fields = '__all__'

    def validate(self, attrs):
        queryset = Favourite.objects.filter(
            post=attrs["post"], user=attrs["user"])
        if queryset.exists():
            raise serializers.ValidationError("already")
        return attrs
