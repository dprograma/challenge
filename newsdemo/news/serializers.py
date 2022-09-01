from rest_framework import serializers
from .models import DemoNewsModel


class NewsIdSerializer(serializers.ModelSerializer):

    class Meta:
        model = DemoNewsModel
        fields = ('newsid', 'name', 'relatedids', 'score', 'title', 'newstype', 'descendants', 'text', 'url', 'created_at')
