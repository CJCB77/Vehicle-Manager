# Generated by Django 5.0.6 on 2024-06-29 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0002_vehicle_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='mileage',
            field=models.PositiveIntegerField(default=0, verbose_name='Mileage'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehicle',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Price'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehicle',
            name='year',
            field=models.PositiveIntegerField(default=2024, verbose_name='Year'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='transmission',
            field=models.CharField(choices=[('automatic', 'Automatic'), ('manual', 'Manual')], verbose_name='Transmission'),
        ),
    ]
