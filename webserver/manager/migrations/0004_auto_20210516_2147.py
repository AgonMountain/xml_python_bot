# Generated by Django 3.2.1 on 2021-05-16 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_auto_20210516_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elementaddition',
            name='addition_element',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addition_to', to='manager.element'),
        ),
        migrations.AlterField(
            model_name='elementaddition',
            name='element',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addition_from', to='manager.element'),
        ),
        migrations.AlterField(
            model_name='elementtransition',
            name='element',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transition_from', to='manager.element'),
        ),
        migrations.AlterField(
            model_name='elementtransition',
            name='transition_element',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transition_to', to='manager.element'),
        ),
    ]