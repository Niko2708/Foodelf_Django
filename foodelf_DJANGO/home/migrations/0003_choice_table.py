# Generated by Django 2.1.7 on 2019-03-12 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manageTables', '0001_initial'),
        ('home', '0002_choice_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='table',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='manageTables.ActiveTables'),
        ),
    ]
