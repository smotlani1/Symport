# Generated by Django 4.0.4 on 2022-04-21 23:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logbook2', '0006_alter_logbookentry2_logbook'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logbookentry2',
            name='logbook',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='logbook2.logbook2'),
        ),
    ]
