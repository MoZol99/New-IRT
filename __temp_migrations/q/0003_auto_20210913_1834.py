# Generated by Django 2.2.12 on 2021-09-13 15:34

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('q', '0002_auto_20210913_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='fin_situation_change',
            field=otree.db.models.StringField(blank=True, max_length=10000, null=True, verbose_name='Did your family financial situation change over the last year - How would you answer the previous question a year ago?'),
        ),
    ]
