# Generated by Django 4.2.8 on 2023-12-10 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockapp', '0003_sqlmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sqlmodel',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
