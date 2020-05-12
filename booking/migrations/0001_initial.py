# Generated by Django 3.0.5 on 2020-05-12 08:06

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='full name')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='HealthStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cough', models.BooleanField(default=False)),
                ('cold', models.BooleanField(default=False)),
                ('diarrhea', models.BooleanField(default=False)),
                ('sore_throat', models.BooleanField(default=False)),
                ('body_aches', models.BooleanField(default=False)),
                ('headache', models.BooleanField(default=False)),
                ('fever', models.BooleanField(default=False)),
                ('difficult_breath', models.BooleanField(default=False)),
                ('traveled', models.BooleanField(default=False)),
                ('infected_trip', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Health Status',
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_available', models.BooleanField(default=False)),
                ('day', models.CharField(max_length=50)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='ServiceProvider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=50)),
                ('lga', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=254)),
                ('desc', models.TextField(verbose_name='description')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('email', models.EmailField(max_length=50)),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.Schedule')),
            ],
            options={
                'ordering': ('name', 'state', 'lga'),
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=50)),
                ('lga', models.CharField(max_length=50)),
                ('date', models.DateTimeField()),
                ('confirmed', models.BooleanField(default=False)),
                ('booker', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='booking.Booker')),
                ('service_provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.ServiceProvider')),
            ],
            options={
                'ordering': ('date',),
            },
        ),
        migrations.AddField(
            model_name='booker',
            name='health_status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='booking.HealthStatus'),
        ),
    ]
