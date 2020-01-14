# Generated by Django 3.0.2 on 2020-01-14 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('apleId', models.IntegerField(verbose_name='apleId')),
                ('genres', models.ManyToManyField(blank=True, to='core.Genre', verbose_name='Genres')),
            ],
            options={
                'verbose_name': 'Artist',
                'verbose_name_plural': 'Artists',
            },
        ),
    ]