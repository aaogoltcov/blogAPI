from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Post(models.Model):
    """
    Новостной пост блога, с указанием названия, текста и даты
    """
    title = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s %s" % (self.title, self.text)

    class Meta:
        ordering = ['date']
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Comment(MPTTModel):
    """
    Комментарий к посту или к другому комментарию
    """
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return "%s %s" % (self.text, self.parent)

    class Meta:
        ordering = ['date']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    class MPTTMeta:
        order_insertion_by = ['parent']
