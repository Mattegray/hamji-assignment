# Generated by Django 3.2.9 on 2021-12-05 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0016_alter_choice_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
