from django.db import models

# Create your models here.
class PostsModel(models.Model):
    class Meta:
        db_table = 'blog_posts'
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
    title = models.CharField(max_length=255, verbose_name='Title')
    content = models.TextField(verbose_name='Content')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created')

    def __str__(self):
        return f"{self.title} - created at {self.date_created}"
