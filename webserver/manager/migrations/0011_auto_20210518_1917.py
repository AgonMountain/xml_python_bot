# Generated by Django 3.2.1 on 2021-05-18 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0010_alter_config_messenger'),
    ]

    operations = [
        migrations.AlterField(
            model_name='config',
            name='messenger',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='manager.messenger'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='config',
            name='token',
            field=models.CharField(default='', max_length=100, verbose_name='Токен'),
            preserve_default=False,
        ),
    ]