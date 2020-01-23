# Generated by Django 2.2.7 on 2019-12-01 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('allinfo', '0004_auto_20191201_1128'),
    ]

    operations = [
        migrations.CreateModel(
            name='Routine_days',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
            ],
        ),
        migrations.CreateModel(
            name='Routine_time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_days', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
            ],
        ),
        migrations.CreateModel(
            name='Room_with_na',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_no', models.CharField(max_length=120)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('routine_days', models.ForeignKey(on_delete='DO_NOTHING', to='routine_info.Routine_days')),
                ('routine_time', models.ForeignKey(on_delete='DO_NOTHING', to='routine_info.Routine_time')),
                ('teacher_initial', models.ForeignKey(on_delete='DO_NOTHING', to='allinfo.Techer_info')),
            ],
        ),
    ]