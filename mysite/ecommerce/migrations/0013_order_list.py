# Generated by Django 4.1.1 on 2022-10-02 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0012_delete_order_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order_list',
            fields=[
                ('date_ordered', models.DateTimeField(auto_now_add=True, null=True)),
                ('complete', models.BooleanField(default=True)),
                ('rent_from', models.DateTimeField(null=True)),
                ('rent_to', models.DateTimeField(null=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ecommerce.customer')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ecommerce.product')),
            ],
        ),
    ]
