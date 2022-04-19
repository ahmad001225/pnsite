from rest_framework import serializers
from blog.models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    comment = serializers.HyperlinkedRelatedField (
        many=True,
        read_only=True,
        view_name='comment-detail'
    )
    class Meta:
        model = Post
        fields = '__all__'


