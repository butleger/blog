from django.db import models
from tinymce.models import HTMLField
from ckeditor.fields import RichTextField


class MyModel(models.Model):
    content = RichTextField()


class ArticleModel(models.Model):
    title = models.CharField(max_length=50)
    text = RichTextField()
    date = models.DateTimeField()
    likes = models.IntegerField(default=0)


    class Meta:
        verbose_name_plural = 'Cтатья'


    def __str__(self):
        return self.title


class CommentModel(models.Model):
    author = models.CharField(max_length=20, default='Anonim')
    text = models.TextField()
    article = models.ForeignKey(ArticleModel, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    date = models.DateTimeField()

    def __str__(self):
        return self.author


class MainMenuElementModel(models.Model):
    ref = models.CharField(max_length=30)
    text = models.CharField(max_length=20)

    def __str__(self):
        return self.text


class FooterBlockModel(models.Model):
    name = models.CharField(max_length=20, default='defaultName')

    def __str__(self):
        return self.name


class FooterContentModel(models.Model):
    text = models.CharField(max_length=20)
    ref = models.CharField(max_length=30)
    footerBlock = models.ForeignKey(FooterBlockModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

# Create your models here.
