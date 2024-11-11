from django.db import models
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length= 256)
    is_published  = models.BooleanField(default=True)


class Article(models.Model):
    title = models.CharField(max_length=256)
    is_published = models.BooleanField(default=True)
    time_publish = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True)
    slug = models.CharField(max_length=256, null=True, unique=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save (self,*arg, **kwargs):
        self.slug = self.addslug()
        super(Article,self).save(*arg, **kwargs)

    def addslug(title):
        return slugify(title)
    
    def __str__(self) -> str:
        return self.title
