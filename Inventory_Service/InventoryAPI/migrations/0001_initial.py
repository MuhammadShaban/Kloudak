# Generated by Django 2.0.5 on 2018-05-23 22:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('subnet', models.CharField(max_length=100)),
                ('next_ip', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vm_can_add', models.BooleanField()),
                ('vm_can_edit', models.BooleanField()),
                ('vm_can_delete', models.BooleanField()),
                ('network_can_add', models.BooleanField()),
                ('network_can_edit', models.BooleanField()),
                ('network_can_delete', models.BooleanField()),
                ('router_can_add', models.BooleanField()),
                ('router_can_edit', models.BooleanField()),
                ('router_can_delete', models.BooleanField()),
                ('user_can_add', models.BooleanField()),
                ('user_can_edit', models.BooleanField()),
                ('user_can_delete', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FreeIP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=200)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='f_area', to='InventoryAPI.Area')),
            ],
        ),
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(blank=True, max_length=300)),
                ('state', models.CharField(choices=[('U', 'Up'), ('C', 'Creating')], default='C', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Router',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='RouterInterface',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=200)),
                ('network', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='iface', to='InventoryAPI.Network')),
                ('router', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='router', to='InventoryAPI.Router')),
            ],
        ),
        migrations.CreateModel(
            name='VM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(blank=True, max_length=300)),
                ('ip', models.CharField(max_length=200)),
                ('state', models.CharField(choices=[('C_D', 'Creating_Disk'), ('C_N', 'Configuring_Network'), ('U', 'UP'), ('D', 'Down')], default='C_D', max_length=20)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='area', to='InventoryAPI.Area')),
                ('networks', models.ManyToManyField(to='InventoryAPI.Network')),
            ],
        ),
        migrations.CreateModel(
            name='VMTemplate',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('os', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=300)),
                ('cpu', models.IntegerField()),
                ('ram', models.IntegerField()),
                ('disk', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Workspace',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='vm',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vm_workspace', to='InventoryAPI.Workspace'),
        ),
        migrations.AddField(
            model_name='vm',
            name='template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='template', to='InventoryAPI.VMTemplate'),
        ),
        migrations.AddField(
            model_name='router',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='r_workspace', to='InventoryAPI.Workspace'),
        ),
        migrations.AddField(
            model_name='network',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='n_workspace', to='InventoryAPI.Workspace'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='workspace',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='InventoryAPI.Workspace'),
        ),
        migrations.AlterUniqueTogether(
            name='vm',
            unique_together={('name', 'owner')},
        ),
        migrations.AlterUniqueTogether(
            name='routerinterface',
            unique_together={('network', 'router')},
        ),
        migrations.AlterUniqueTogether(
            name='router',
            unique_together={('name', 'owner')},
        ),
        migrations.AlterUniqueTogether(
            name='network',
            unique_together={('name', 'owner')},
        ),
        migrations.AlterUniqueTogether(
            name='customuser',
            unique_together={('user', 'workspace')},
        ),
    ]
