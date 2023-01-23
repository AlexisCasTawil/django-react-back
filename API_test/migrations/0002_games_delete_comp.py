# Generated by Django 4.1.5 on 2023-01-19 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API_test', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cathegory', models.CharField(max_length=30)),
                ('website', models.CharField(max_length=80)),
                ('company', models.CharField(max_length=60)),
            ],
        ),
        migrations.DeleteModel(
            name='comp',
        ),
    ]