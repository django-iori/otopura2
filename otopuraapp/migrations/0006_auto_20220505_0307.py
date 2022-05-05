# Generated by Django 3.2.6 on 2022-05-04 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('otopuraapp', '0005_auto_20220430_0247'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentmodel',
            name='cm_band',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, related_name='cm_band', to='otopuraapp.bandmodel'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='goodmodel',
            name='good_band',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, related_name='good_band', to='otopuraapp.bandmodel'),
            preserve_default=False,
        ),
    ]
