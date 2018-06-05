from rest_framework import serializers
from myapp.models import Post

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'text', 'author', 'created_date', 'modified_date', 'published_date')
