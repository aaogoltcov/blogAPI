from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from post.models import Post, Comment


@admin.register(Post)
class PhotoAdmin(admin.ModelAdmin):
    pass


admin.site.register(Comment, MPTTModelAdmin)
