# Generated by Django 3.2.1 on 2021-05-18 22:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0014_auto_20210518_1927'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='config',
            options={'verbose_name': 'Конфигурация', 'verbose_name_plural': '2_Конфигурации'},
        ),
        migrations.AlterModelOptions(
            name='element',
            options={'verbose_name': 'Элемент', 'verbose_name_plural': '5_Элементы'},
        ),
        migrations.AlterModelOptions(
            name='elementaddition',
            options={'verbose_name': 'Дополнение', 'verbose_name_plural': '6_Дополнения'},
        ),
        migrations.AlterModelOptions(
            name='elementtransition',
            options={'verbose_name': 'Переход', 'verbose_name_plural': '7_Переходы'},
        ),
        migrations.AlterModelOptions(
            name='messenger',
            options={'verbose_name': 'Мессенджер', 'verbose_name_plural': '1_Мессенджеры'},
        ),
        migrations.AlterModelOptions(
            name='scheme',
            options={'verbose_name': 'Схема', 'verbose_name_plural': '4_Схемы'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': '3_Пользователи'},
        ),
    ]