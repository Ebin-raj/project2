# Generated by Django 4.2.1 on 2023-06-05 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_alter_cartitem_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='image',
        ),
    ]
