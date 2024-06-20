from rest_framework import serializers

from person.models import Person


class FamousSerializers(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('name', 'content')