# Generated by Django 3.1.3 on 2023-05-05 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laundryapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pagetitle', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='laundry',
            name='todate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
