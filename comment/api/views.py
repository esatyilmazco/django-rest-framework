from rest_framework.generics import CreateAPIView, ListAPIView
from comment.models import Comment
from comment.api.serializers import CommentCreateSerializer, CommentListSerializer


class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer

    def perform_create(self, serializers):
        serializers.save(user=self.request.user)


class CommentListAPIView(ListAPIView):
    serializer_class = CommentListSerializer

    def get_queryset(self):
        return Comment.objects.filter(parent=None)