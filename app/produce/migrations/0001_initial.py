# Generated by Django 3.2.9 on 2021-11-17 01:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('farm', '0006_auto_20211109_1833'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('min_quantity', models.FloatField()),
                ('is_organic', models.BooleanField()),
                ('farm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farm.farm')),
            ],
        ),
    ]
