# Generated by Django 3.2 on 2022-09-15 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Estados',
            },
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomenclatura', models.CharField(max_length=50, unique=True)),
                ('descripcion', models.CharField(max_length=500)),
                ('fechaestado', models.DateField(null=True)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='documentos.estado')),
            ],
            options={
                'verbose_name_plural': 'Documentos',
            },
        ),
    ]