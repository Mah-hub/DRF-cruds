# Generated by Django 4.1.2 on 2022-12-17 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_alter_item_project'),
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='items',
            field=models.ManyToManyField(to='items.item'),
        ),
    ]
