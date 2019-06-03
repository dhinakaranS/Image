# Generated by Django 2.2.1 on 2019-06-03 10:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('user_name', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=20)),
                ('created_on', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
