from rest_framework import serializers

from .models import User, Token, Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ("_id", "name", "link")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = "__all__"
