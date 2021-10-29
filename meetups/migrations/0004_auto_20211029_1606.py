# Generated by Django 3.2.8 on 2021-10-29 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0003_auto_20211029_1231'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='meetup',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meetups.location'),
        ),
        migrations.AddField(
            model_name='meetup',
            name='participants',
            field=models.ManyToManyField(blank=True, null=True, to='meetups.Participant'),
        ),
    ]
