# Generated by Django 4.2.4 on 2023-08-18 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshopping', '0005_alter_author_recommendedby'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='followers',
            field=models.ManyToManyField(blank=True, null=True, related_name='followed_authors', related_query_name='followed_authors', to='eshopping.user'),
        ),
    ]
