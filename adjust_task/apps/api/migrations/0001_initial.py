# Generated by Django 3.2.1 on 2021-05-09 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, db_index=True, null=True, verbose_name='date')),
                ('channel', models.CharField(blank=True, max_length=50, verbose_name='channel')),
                ('country', models.CharField(blank=True, max_length=10, verbose_name='country')),
                ('os', models.CharField(blank=True, max_length=10, verbose_name='os')),
                ('impressions', models.PositiveIntegerField(blank=True, null=True, verbose_name='impressions')),
                ('clicks', models.PositiveIntegerField(blank=True, null=True, verbose_name='clicks')),
                ('installs', models.PositiveIntegerField(blank=True, null=True, verbose_name='installs')),
                ('spend', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='spend')),
                ('revenue', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='revenue')),
                ('created_at', models.DateField(auto_now_add=True, help_text='the date when dataset was created', verbose_name='created_at')),
            ],
            options={
                'verbose_name': 'dataset',
                'verbose_name_plural': 'datasets',
            },
        ),
    ]
