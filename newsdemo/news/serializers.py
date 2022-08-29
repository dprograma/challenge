from rest_framework import serializers
from .models import HackerNewsID


class NewsIdSerializer(serializers.ModelSerializer):

    class Meta:
        model = HackerNewsID
        fields = ('hackernews',)
