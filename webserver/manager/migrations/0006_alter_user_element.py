# Generated by Django 3.2.1 on 2021-05-16 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0005_auto_20210516_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='element',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='manager.element'),
        ),
    ]