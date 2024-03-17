# Generated by Django 5.0.2 on 2024-03-04 13:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(db_index=True, max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Tests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('review', models.TextField(blank=True)),
                ('manual', models.TextField(blank=True)),
                ('number_of_questions', models.IntegerField()),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='constructor.categories')),
            ],
            options={
                'verbose_name': 'Тесты',
                'verbose_name_plural': 'Тесты',
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=250)),
                ('result', models.IntegerField()),
                ('the_best_result', models.IntegerField()),
                ('test', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='constructor.tests')),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_ordinal', models.IntegerField(default=1)),
                ('question_text', models.TextField(blank=True)),
                ('test', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='constructor.tests')),
            ],
        ),
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answers_ordinal', models.IntegerField(default=1)),
                ('answers_text', models.TextField(blank=True)),
                ('answers_weight', models.IntegerField(default=1)),
                ('question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='constructor.questions')),
                ('test', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='constructor.tests')),
            ],
        ),
        migrations.CreateModel(
            name='Valuation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valuation', models.CharField(max_length=250)),
                ('value_min', models.IntegerField()),
                ('value_max', models.IntegerField()),
                ('analysis', models.TextField(blank=True)),
                ('test', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='constructor.tests')),
            ],
        ),
    ]