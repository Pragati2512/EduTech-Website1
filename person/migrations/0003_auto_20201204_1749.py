# Generated by Django 3.1.4 on 2020-12-04 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0002_doubt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doubt',
            name='answer',
            field=models.TextField(default='Unanswered'),
        ),
    ]
