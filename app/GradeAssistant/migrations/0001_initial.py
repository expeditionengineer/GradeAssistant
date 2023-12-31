# Generated by Django 5.0 on 2023-12-14 10:44

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('className', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField(blank=True, choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14)], default=0)),
                ('weight', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)])),
                ('parent', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='GradeAssistant.grade')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=30)),
                ('lastName', models.CharField(max_length=30)),
                ('classRelation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GradeAssistant.class')),
                ('grades', models.ManyToManyField(to='GradeAssistant.grade')),
            ],
        ),
        migrations.AddField(
            model_name='grade',
            name='students',
            field=models.ManyToManyField(to='GradeAssistant.student'),
        ),
    ]
