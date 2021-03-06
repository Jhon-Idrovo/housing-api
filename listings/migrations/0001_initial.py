# Generated by Django 3.1.7 on 2021-04-10 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='OpertationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PropertyType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='listings.city')),
            ],
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='listings.country')),
            ],
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_type', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('created_on', models.DateField()),
                ('lat', models.DecimalField(decimal_places=8, max_digits=14)),
                ('lon', models.DecimalField(decimal_places=8, max_digits=14)),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.IntegerField()),
                ('surface_total', models.IntegerField()),
                ('surface_covered', models.IntegerField()),
                ('price', models.IntegerField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listings.city')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listings.country')),
                ('operation_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listings.opertationtype')),
                ('property_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listings.propertytype')),
                ('province', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listings.province')),
                ('zone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listings.zone')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='province',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='listings.province'),
        ),
    ]
