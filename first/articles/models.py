from django.db import models
from tinymce.models import HTMLField
from ckeditor.fields import RichTextField


class CategoryModel(models.Model):
    name = models.CharField(max_length=20,
                            default='Other')

    # make default value for article
    OTHER_CATEGORY_ID = 1

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'

    def __str__(self):
        return self.name


class ArticleModel(models.Model):
    category = models.ForeignKey(CategoryModel,
                                 on_delete=models.CASCADE,
                                 default=CategoryModel.OTHER_CATEGORY_ID)
    title = models.CharField(max_length=50)
    text = RichTextField()
    date = models.DateTimeField()
    likes = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Cтатьи'
        verbose_name = 'Cтатья'

    def __str__(self):
        return self.title


class ArticleTagModel(models.Model):
    name = models.CharField(max_length=20)
    article = models.ForeignKey(ArticleModel,
                                on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Теги статей'
        verbose_name = 'Тег статьи'

    def __str__(self):
        return self.name


class CommentModel(models.Model):
    author = models.CharField(max_length=20, default='Anonim')
    text = models.TextField()
    article = models.ForeignKey(ArticleModel, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    date = models.DateTimeField()

    class Meta:
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.author


class MainMenuElementModel(models.Model):
    ref = models.CharField(max_length=30)
    text = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'Элементы навигации хедера'
        verbose_name = 'Элемент навигации хедера'

    def __str__(self):
        return self.text


class FooterBlockModel(models.Model):
    name = models.CharField(max_length=20, default='defaultName')

    class Meta:
        verbose_name_plural = 'Блоки в футере'
        verbose_name = 'Блок в футере'

    def __str__(self):
        return self.name


class FooterContentModel(models.Model):
    text = models.CharField(max_length=20)
    ref = models.CharField(max_length=30)
    footerBlock = models.ForeignKey(FooterBlockModel, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Элементы блока в футере'
        verbose_name = 'Элемент блока в футере'

    def __str__(self):
        return self.text


class SingleArticleModel(models.Model):
    name = models.CharField(max_length=30, unique=True)
    text = RichTextField()

    class Meta:
        verbose_name_plural = 'Одиночные статьи'
        verbose_name = 'Одиночные статьи'

    def __str__(self):
        return self.name
# Create your models here.
