from rest_framework import serializers
from bovine.models import Bovine

class BovineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bovine
        fields = ['id', 'distinctiveTrait', 'breed', 'is_female', 'dateOfBirth']

