from rest_framework import serializers
from .models import Movie


# Defines a new class, BookSerializer, which subclasses serializers.ModelSerializer. This means that the BookSerializer class inherits all the behavior of serializers.ModelSerializer, but can also add or override behavior as needed.
class MovieSerializer(serializers.ModelSerializer):
    # Defines an inner class, Meta, which is used to specify metadata about the serializer class.
    class Meta:
        # Specifies the fields from the Thing model that should be included in the serialized representation.
        fields = ('id', 'owner', 'Title', 'Genre', 'created_at')
        # Specifies the model that the serializer should use to generate the serialized representation. This is the Thing model that we imported earlier.
        model = Movie