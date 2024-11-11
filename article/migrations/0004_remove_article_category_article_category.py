# Generated by Django 5.1.1 on 2024-11-02 15:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_alter_article_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='Category',
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='article.category'),
        ),
    ]