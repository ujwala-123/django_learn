# Generated by Django 4.2.4 on 2023-08-18 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshopping', '0002_course_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='followers',
            field=models.ManyToManyField(null=True, related_name='followed_authors', related_query_name='followed_authors', to='eshopping.user'),
        ),
    ]
