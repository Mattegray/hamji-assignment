# Generated by Django 3.2.9 on 2021-12-03 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_question_closed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='closed_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='date closed'),
        ),
    ]
