# Generated by Django 5.1.1 on 2024-11-02 16:00

from django.db import migrations

def create_iniial_categories (apps, schema_editor):
    list_categories = ["News",
                       "Business",
                       "Sports",
                       "Health",
                       ]
    
    Category = apps.get_model('article', 'Category')
    for title in list_categories:
        Category.objects.create(title=title, is_published=True)

class Migration(migrations.Migration):
    dependencies = [
        ('article', '0004_remove_article_category_article_category'),
    ]

    operations = [
        migrations.RunPython(create_iniial_categories),
    ]