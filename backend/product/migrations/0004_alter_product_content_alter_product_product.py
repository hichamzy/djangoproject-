# Generated by Django 4.0.4 on 2022-05-06 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=15),
        ),
    ]