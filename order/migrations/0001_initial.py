# Generated by Django 2.2.6 on 2019-10-30 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dishes', '0002_auto_20191030_1146'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('price', models.DecimalField(decimal_places=2, default=True, max_digits=9)),
                ('place_delivery', models.CharField(max_length=512)),
                ('user_profile', models.CharField(max_length=512)),
                ('dishes', models.ManyToManyField(blank=True, null=True, to='dishes.Dish')),
                ('drinks', models.ManyToManyField(blank=True, null=True, to='dishes.Drink')),
            ],
        ),
    ]