# Generated by Django 2.2.3 on 2019-07-16 21:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190716_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='answer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Answer'),
        ),
    ]
