# Generated by Django 2.1 on 2019-02-28 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('screen', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie_Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='')),
                ('video_title', models.CharField(max_length=100)),
            ],
        ),
    ]