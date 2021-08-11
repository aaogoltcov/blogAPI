from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from post.models import Post, Comment
from post.serializer import PostSerializer, CommentCreateSerializer, CommentViewSerializer


def generate_dict_of_comments(db_query, level=None):
    new_list_of_dicts = []

    def generate_comments_layers(current_layer, source):
        current_layer['child'] = []
        for _ in source:
            if _['parent'] == current_layer['id'] and (level is None or _['level'] <= level):
                current_layer['child'].append(_)
                generate_comments_layers(current_layer['child'][-1], source)

    for _ in db_query:
        if _['parent'] is None:
            new_list_of_dicts.append(_)
            generate_comments_layers(_, db_query)

    return new_list_of_dicts


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
        all_comments_for_post = CommentViewSerializer(Comment.objects.filter(post=kwargs['pk']), many=True).data
        new_list_of_comments_of_post = generate_dict_of_comments(all_comments_for_post)
        return Response(new_list_of_comments_of_post)


class CommentListMaxLevel(generics.ListAPIView):
    """
    COMMENT LIST MAX LEVEL - получение информации о всех комментариях для выбранного поста
    не выше указанного уровня
    """
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentViewSerializer

    def list(self, request, *args, **kwargs):
        all_comments_for_post = CommentViewSerializer(Comment.objects.filter(post=kwargs['pk']), many=True).data
        new_list_of_comments_of_post = generate_dict_of_comments(all_comments_for_post, kwargs['pk_sub'])
        return Response(new_list_of_comments_of_post)


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
        all_comments_for_post = CommentViewSerializer(Comment.objects.all(), many=True).data
        new_list_of_comments_of_post = generate_dict_of_comments(all_comments_for_post, kwargs['pk'])
        return Response(new_list_of_comments_of_post)
