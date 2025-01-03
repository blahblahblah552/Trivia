# Generated by Django 5.1.4 on 2024-12-29 19:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('correctlyAnswered', models.PositiveIntegerField(default=0)),
                ('incorrectlyAnswered', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('true_or_false', models.BooleanField(default=False)),
                ('difficulty', models.CharField(choices=[('E', 'Easy'), ('M', 'Medium'), ('H', 'Hard')], default='M', max_length=2)),
                ('question_text', models.CharField(max_length=40)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('count', models.PositiveIntegerField(default=0)),
                ('category', models.ManyToManyField(to='trivia.category')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=80)),
                ('correct', models.BooleanField(default=False)),
                ('question_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trivia.question')),
            ],
        ),
    ]
