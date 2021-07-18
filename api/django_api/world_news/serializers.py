from rest_framework import serializers
from world_news.models import Snippet,Schema_test,Table_test


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code')


class Schema_testSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schema_test
        fields = ('schema_name', 'describe', 'term_of_use')

class Table_testSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table_test
        fields = ('table_name', 'describe')