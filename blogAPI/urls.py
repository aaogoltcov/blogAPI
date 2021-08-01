from django.contrib import admin
from django.urls import path

from post.views import PostList, PostInfo, PostCreate, CommentCreate, CommentList, CommentListMaxLevel, \
    AllCommentsWithLevel

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts', PostList.as_view()),
    path('post/<int:pk>', PostInfo.as_view()),
    path('create', PostCreate.as_view()),
    path('comment', CommentCreate.as_view()),
    path('comments/<int:pk>', CommentList.as_view()),
    path('level_max/<int:pk>/<int:pk_sub>', CommentListMaxLevel.as_view()),
    path('level_comments/<int:pk>', AllCommentsWithLevel.as_view()),
]
