# Generated by Django 3.1 on 2020-08-12 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0015_auto_20200812_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlemodel',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='articles.categorymodel'),
        ),
        migrations.AlterField(
            model_name='categorymodel',
            name='name',
            field=models.CharField(default='Other', max_length=20, unique=True),
        ),
    ]
