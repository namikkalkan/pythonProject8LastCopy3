# Generated by Django 4.1.1 on 2022-10-02 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0005_alter_order_rent_from_alter_order_rent_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='rent_from',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='rent_to',
            field=models.DateTimeField(null=True),
        ),
    ]
