# Generated by Django 3.0 on 2019-12-15 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_offer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image_url',
            field=models.ImageField(blank=True, upload_to='image_fruit'),
        ),
    ]