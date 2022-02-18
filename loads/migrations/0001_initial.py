# Generated by Django 4.0.2 on 2022-02-10 02:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=255)),
                ('street', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('zip', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=255)),
                ('street', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('zip', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('amount_invoiced', models.DecimalField(decimal_places=2, max_digits=7)),
                ('amount_paid', models.DecimalField(decimal_places=2, max_digits=7)),
                ('payment_status', models.CharField(choices=[('N', 'Not Invoiced'), ('I', 'Invoices'), ('P', 'Paid')], default='N', max_length=3)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='loads.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Load',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_street', models.CharField(max_length=255)),
                ('start_city', models.CharField(max_length=255)),
                ('start_state', models.CharField(max_length=255)),
                ('start_zip', models.CharField(max_length=255)),
                ('end_street', models.CharField(max_length=255)),
                ('end_city', models.CharField(max_length=255)),
                ('end_state', models.CharField(max_length=255)),
                ('end_zip', models.CharField(max_length=255)),
                ('loaded_distance', models.IntegerField()),
                ('hazmat', models.BooleanField(default=False)),
                ('load_reference', models.TextField(null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='loads.customer')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='loads.driver')),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='loads.invoice')),
            ],
        ),
    ]