# Generated by Django 2.0.2 on 2018-03-22 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ControllerAPI', '0002_auto_20180322_1053'),
    ]

    operations = [
        migrations.CreateModel(
            name='vmTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=200)),
                ('finished', models.BooleanField(default=False)),
                ('created', models.DateTimeField()),
                ('modified', models.DateTimeField()),
                ('netConf', models.BooleanField(default=False)),
                ('vmConf', models.BooleanField(default=False)),
                ('objectName', models.CharField(max_length=200)),
                ('method', models.CharField(choices=[('POST', 'POST'), ('PUT', 'PUT'), ('DELETE', 'DELETE')], max_length=20)),
                ('task', models.TextField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Task',
            new_name='networkTask',
        ),
    ]
