from rest_framework import serializers
from .models import DemoNewsModel


class NewsIdSerializer(serializers.ModelSerializer):

    class Meta:
        model = DemoNewsModel
        fields = ('hackernews',)
