# Generated by Django 3.2.13 on 2022-06-09 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_book_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='naz',
        ),
        migrations.AddField(
            model_name='author',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='authors/%Y-%m-%d/'),
        ),
    ]
