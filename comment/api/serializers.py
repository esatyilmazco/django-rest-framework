from rest_framework.serializers import ModelSerializer, SerializerMethodField
from comment.models import Comment
from rest_framework import fields, serializers
from django.contrib.auth.models import User
from post.models import Post


class CommentCreateSerializer(ModelSerializer):
    class Meta:
        model = Comment
        exclude = ['created', ]

    def validate(self, attrs):
        if (attrs["parent"]):
            if attrs["parent"].post != attrs["post"]:
                raise serializers.validationError("something vent wrong")
        return attrs


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ['password', ]


class PostCommentSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'id')


class CommentListSerializer(ModelSerializer):
    replies = SerializerMethodField()
    user = UserSerializer()
    post = PostCommentSerializer()

    class Meta:
        model = Comment
        fields = '__all__'

    def get_replies(self, obj):
        if obj.any_children:
            return CommentListSerializer(obj.children(), many=True).data


class CommentDeleteUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['content']
