# Generated by Django 3.1.7 on 2021-03-23 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facname', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=255)),
                ('nickname', models.CharField(max_length=100)),
                ('birthday', models.DateField(verbose_name='birthday date')),
                ('facname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile_management.faculty')),
            ],
        ),
    ]