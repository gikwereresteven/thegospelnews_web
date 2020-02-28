# Generated by Django 2.2.5 on 2020-02-10 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GospelApp', '0003_auto_20200121_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Video', models.FileField(upload_to='videos')),
                ('video_title', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
