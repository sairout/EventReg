# Generated by Django 3.0.4 on 2020-05-21 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('reg_id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=150)),
                ('mobile', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=100)),
                ('identification', models.ImageField(upload_to='ids')),
                ('reg_type', models.CharField(max_length=20)),
                ('no_ticket', models.IntegerField()),
                ('reg_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
