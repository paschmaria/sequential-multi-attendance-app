# Generated by Django 3.0.5 on 2020-05-13 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_auto_20200513_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='schedule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.Schedule'),
        ),
    ]
