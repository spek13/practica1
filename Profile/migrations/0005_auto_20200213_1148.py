# Generated by Django 2.0.13 on 2020-02-13 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0004_auto_20200213_1038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='example3',
            name='estado_civil',
        ),
        migrations.AlterField(
            model_name='example3',
            name='ciudad',
            field=models.CharField(max_length=254),
        ),
        migrations.AlterField(
            model_name='example3',
            name='estado',
            field=models.CharField(max_length=254),
        ),
        migrations.AlterField(
            model_name='example3',
            name='genero',
            field=models.CharField(max_length=254),
        ),
        migrations.AlterField(
            model_name='example3',
            name='ocupacion',
            field=models.CharField(max_length=254),
        ),
    ]