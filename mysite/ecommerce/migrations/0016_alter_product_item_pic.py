# Generated by Django 4.1.1 on 2022-10-03 04:41

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0015_alter_product_item_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='item_pic',
            field=django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, null=True, quality=-1, scale=None, size=[640, 480], upload_to=''),
        ),
    ]
