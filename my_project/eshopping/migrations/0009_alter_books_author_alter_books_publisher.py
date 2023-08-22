# Generated by Django 4.2.4 on 2023-08-18 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eshopping', '0008_alter_books_author_alter_books_publisher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', related_query_name='books', to='eshopping.author'),
        ),
        migrations.AlterField(
            model_name='books',
            name='publisher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', related_query_name='books', to='eshopping.publisher'),
        ),
    ]