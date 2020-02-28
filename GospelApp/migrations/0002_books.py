# Generated by Django 2.2.5 on 2020-01-21 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GospelApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_photho', models.CharField(max_length=100)),
                ('book_title', models.CharField(max_length=100)),
                ('book_author', models.CharField(max_length=100)),
                ('book_summary', models.TextField()),
            ],
            options={
                'verbose_name': 'book',
                'verbose_name_plural': 'book',
            },
        ),
    ]
