

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from favourite.models import Favourite


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


class FavouriteAPISerilazer(ModelSerializer):
    class Meta:
        model = Favourite
        fields = '__all__'
