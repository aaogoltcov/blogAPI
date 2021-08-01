from django.db.models import Max
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from post.models import Post, Comment
from post.serializer import PostSerializer, CommentCreateSerializer, CommentViewSerializer


class PostList(generics.ListAPIView):
    """
    POST LIST - получение информации о постах
    """
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def list(self, request, *args, **kwargs):
        return Response(PostSerializer(self.get_queryset(), many=True).data)


class PostInfo(generics.ListAPIView):
    """
    POST INFO - получение информации о конкретном посте
    """
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def list(self, request, *args, **kwargs):
        return Response(PostSerializer(self.get_queryset().filter(id=kwargs['pk']), many=True).data)


class PostCreate(generics.CreateAPIView):
    """
    POST CREATE - размещение поста
    """
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentCreate(generics.CreateAPIView):
    """
    COMMENT CREATE - размещение комментария
    """
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer

    def perform_create(self, serializer, **kwargs):
        if self.request.data['post'] == '':
            return serializer.save(
                post_id=Comment.objects.filter(id=self.request.data['parent']).values('post')[0]['post'])
        else:
            return serializer.save()


class CommentList(generics.ListAPIView):
    """
    COMMENT LIST - получение информации о всех комментариях для выбранного поста
    """
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentViewSerializer

    def list(self, request, *args, **kwargs):
        comment_list = Comment.objects.filter(post=kwargs['pk'])
        comment_tree = comment_list.filter(level=comment_list.aggregate(Max('level'))['level__max'])
        return Response(CommentViewSerializer(comment_tree, many=True).data)


class CommentListMaxLevel(generics.ListAPIView):
    """
    COMMENT LIST MAX LEVEL - получение информации о всех комментариях для выбранного поста не выше указанного уровня
    """
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentViewSerializer

    def list(self, request, *args, **kwargs):
        level_max = Comment.objects.filter(post=kwargs['pk']).filter(level=kwargs['pk_sub'])
        return Response(CommentViewSerializer(level_max, many=True).data)


class AllCommentsWithLevel(generics.ListAPIView):
    """
    COMMENT LIST FOR ALL POSTS FOR TARGET LEVEL - получение информации о всех комментариях
    для всех постов указанного уровня
    """
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentViewSerializer

    def list(self, request, *args, **kwargs):
        level_comment = Comment.objects.filter(level=kwargs['pk'])
        return Response(CommentViewSerializer(level_comment, many=True).data)
