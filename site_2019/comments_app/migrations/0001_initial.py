# Generated by Django 2.2.5 on 2019-09-21 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommentsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=128)),
                ('message', models.CharField(max_length=3000)),
                ('timedate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
