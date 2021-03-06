# Generated by Django 3.1 on 2020-08-12 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0016_auto_20200812_1225'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleTagModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.articlemodel')),
            ],
            options={
                'verbose_name': 'Тег статьи',
                'verbose_name_plural': 'Теги статей',
            },
        ),
    ]
