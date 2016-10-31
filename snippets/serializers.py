from __future__ import unicode_literals

from rest_framework import serializers
from snippets.models import LANGUAGE_CHOICES,STYLE_CHOICES,Snippet

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'lineos', 'language', 'style')