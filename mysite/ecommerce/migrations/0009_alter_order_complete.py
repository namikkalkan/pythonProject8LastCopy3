# Generated by Django 4.1.1 on 2022-10-02 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0008_remove_order_transaction_id_alter_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='complete',
            field=models.BooleanField(default=True),
        ),
    ]
