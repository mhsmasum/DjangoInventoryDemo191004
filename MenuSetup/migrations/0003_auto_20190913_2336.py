# Generated by Django 2.2.2 on 2019-09-13 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MenuSetup', '0002_auto_20190913_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appmenu',
            name='ParentMenu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appMenu', to='MenuSetup.AppMenu'),
        ),
    ]
