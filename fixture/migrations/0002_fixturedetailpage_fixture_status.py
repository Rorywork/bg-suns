# Generated by Django 2.2.8 on 2020-01-16 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fixture', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fixturedetailpage',
            name='fixture_status',
            field=models.CharField(default='Upcoming Match', help_text='Fixture status', max_length=100),
            preserve_default=False,
        ),
    ]
