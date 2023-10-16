# Generated by Django 4.2.6 on 2023-10-16 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('name', models.CharField(max_length=255, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Studio',
            fields=[
                ('name', models.CharField(max_length=255, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('title', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('year', models.IntegerField()),
                ('producers', models.ManyToManyField(related_name='movies', to='core.producer')),
                ('studios', models.ManyToManyField(related_name='movies', to='core.studio')),
            ],
        ),
    ]
