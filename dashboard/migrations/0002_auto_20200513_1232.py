# Generated by Django 3.0.5 on 2020-05-13 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('test_center', 'Test Center'), ('supermarket', 'Supermarket')], max_length=50, verbose_name='category type')),
            ],
        ),
        migrations.RemoveField(
            model_name='serviceprovider',
            name='schedule',
        ),
        migrations.DeleteModel(
            name='Schedule',
        ),
        migrations.AddField(
            model_name='serviceprovider',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.Category'),
        ),
    ]
