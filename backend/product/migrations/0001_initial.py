# Generated by Django 4.0.4 on 2022-05-05 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=120)),
                ('content', models.TextField(max_length=120)),
                ('product', models.TextField(max_length=120)),
            ],
        ),
    ]
