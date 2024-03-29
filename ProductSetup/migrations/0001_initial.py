# Generated by Django 2.2.2 on 2019-08-22 22:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('BasicSettings', '0003_countryorigin'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductName', models.CharField(max_length=800)),
                ('ProductDescripTion', models.CharField(max_length=1000)),
                ('ProductSpecification', models.CharField(max_length=1000)),
                ('ProductCode', models.CharField(max_length=100)),
                ('IsActive', models.BooleanField(default=True)),
                ('IsDelete', models.BooleanField(default=False)),
                ('CreateDate', models.DateTimeField(auto_now_add=True)),
                ('CreateBy', models.CharField(blank=True, max_length=500)),
                ('UpdateBy', models.CharField(blank=True, max_length=500)),
                ('UpdateDate', models.DateTimeField(auto_now=True)),
                ('DeleteDate', models.DateTimeField(blank=True)),
                ('DeleteBy', models.CharField(blank=True, max_length=500)),
                ('ProductBrand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BasicSettings.ItemBrand')),
                ('ProductCategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BasicSettings.ItemCategory')),
                ('ProductColor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BasicSettings.ItemColor')),
                ('ProductCountry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BasicSettings.CountryOrigin')),
                ('ProductSize', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BasicSettings.ItemSize')),
                ('ProductUOM', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BasicSettings.UomMaster')),
            ],
        ),
    ]
