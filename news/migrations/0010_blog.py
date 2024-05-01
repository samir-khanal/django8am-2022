# Generated by Django 4.0.6 on 2022-07-27 08:24

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_alter_news_image_alter_setting_favicon_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('intro', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('views', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Blog',
            },
        ),
    ]
