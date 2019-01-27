# Generated by Django 2.1.5 on 2019-01-18 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titolo', models.CharField(max_length=120)),
                ('contenuto', models.TextField()),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField()),
            ],
        ),
    ]
