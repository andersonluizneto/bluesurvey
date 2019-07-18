# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-18 02:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('survey', '0002_auto_20190717_2247'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('explanation', models.TextField(blank=True, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('option_response', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question.OptionResponse')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question.Question')),
            ],
        ),
        migrations.RenameField(
            model_name='survey',
            old_name='clientes',
            new_name='clients',
        ),
        migrations.AlterField(
            model_name='survey',
            name='title',
            field=models.CharField(max_length=300, unique=True),
        ),
        migrations.AddField(
            model_name='answer',
            name='survey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.Survey'),
        ),
    ]
