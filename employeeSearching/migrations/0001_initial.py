# Generated by Django 4.1.1 on 2022-09-22 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('location', models.CharField(max_length=150, null=True, verbose_name='Location')),
                ('email', models.CharField(max_length=150, null=True, verbose_name='Email')),
                ('company', models.CharField(max_length=150, null=True, verbose_name='Company')),
                ('bio', models.CharField(max_length=150, null=True, verbose_name='Bio')),
                ('blog', models.CharField(max_length=150, null=True, verbose_name='Blog')),
                ('userHtmlUrl', models.CharField(max_length=150, null=True, verbose_name='URL')),
            ],
        ),
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Baslik')),
                ('completed', models.BooleanField(verbose_name='Durum')),
            ],
        ),
    ]