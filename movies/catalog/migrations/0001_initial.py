# Generated by Django 3.0.8 on 2020-07-04 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='enter a title name', max_length=200)),
                ('year', models.CharField(max_length=4)),
                ('rating', models.CharField(max_length=7)),
            ],
        ),
    ]