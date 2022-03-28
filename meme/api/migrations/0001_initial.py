# Generated by Django 4.0.3 on 2022-03-28 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('userID', models.AutoField(default=-1, primary_key=True, serialize=False, verbose_name='pk_user')),
                ('username', models.CharField(max_length=36)),
                ('password', models.CharField(max_length=36)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'User',
            },
        ),
    ]
