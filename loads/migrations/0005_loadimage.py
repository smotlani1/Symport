# Generated by Django 4.0.2 on 2022-02-14 23:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loads', '0004_load_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoadImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='loads/images')),
                ('load', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loads.load')),
            ],
        ),
    ]
