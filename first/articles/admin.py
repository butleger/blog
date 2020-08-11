from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.ArticleModel)
admin.site.register(models.MainMenuElementModel)
admin.site.register(models.CommentModel)
admin.site.register(models.FooterBlockModel)
admin.site.register(models.FooterContentModel)
admin.site.register(models.MyModel)