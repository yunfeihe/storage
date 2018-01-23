from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
import markdown
from django.utils.html import strip_tags

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_post_num(self):
        return len(Post.objects.filter(category=self))


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def get_posts_of_self(self):
        
        return self.post_set.all()

class Post(models.Model):
    title = models.CharField(max_length=70)
    body = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    excerpt = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0)


    def __str__(self):
        return self.title

    def get_abs_url(self): #index url namespace
        return reverse('blog:detail', kwargs={'pk': self.pk})

    def get_comments_num(self):
        return len(self.comment_set.all())

    class Meta:
        ordering = ['-created_time']

    def auto_excerpt(self):
        content = markdown.markdown(self.body, extensions=[
                                                         'markdown.extensions.extra',
                                                         'markdown.extensions.codehilite',
                                                         'markdown.extensions.toc',])
        excerpt = strip_tags(content)[:50]
        return excerpt

    def auto_increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

class SinglePage(models.Model):
    title = models.CharField(max_length=70)
    name = models.CharField(max_length=70)
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_body_of_markdown(self):
        return markdown.markdown(self.body, extensions=[
                                                        'markdown.extensions.extra',
                                                        'markdown.extensions.codehilite',
                                                        'markdown.extensions.toc',
            ])
