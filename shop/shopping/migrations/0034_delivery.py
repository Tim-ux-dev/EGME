# Generated by Django 3.0 on 2019-12-27 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0033_remove_sizes_owners'),
    ]

    operations = [
        migrations.CreateModel(
            name='delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charge', models.IntegerField(default=0)),
            ],
        ),
    ]
