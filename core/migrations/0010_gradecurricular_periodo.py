# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-22 14:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_disciplinaofertada'),
    ]

    operations = [
        migrations.CreateModel(
            name='GradeCurricular',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.SmallIntegerField()),
                ('semestre', models.CharField(max_length=1)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gradesCurriculares', to='core.Curso')),
            ],
            options={
                'db_table': 'GradeCurricular',
            },
        ),
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.SmallIntegerField()),
                ('disciplinas', models.ManyToManyField(db_table='PeriodoDisicplina', related_name='periodos', to='core.Disciplina')),
                ('gradeCurricular', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='periodos', to='core.GradeCurricular')),
            ],
            options={
                'db_table': 'Periodo',
            },
        ),
    ]
