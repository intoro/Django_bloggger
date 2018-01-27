# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Enter a article Actors Name (e.g. Tom Cruise, Daniel Radcliff).', max_length=200)),
                ('last_name', models.CharField(max_length=100)),
                ('bio', models.TextField(default='No Bio Information Set', help_text='Enter a brief Character Bio or Resume', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default='SOME STRING', max_length=200, null=True)),
                ('release_date', models.DateField(null=True, blank=True)),
                ('summary', models.TextField(help_text='Enter a brief description of the article, NO SPOILERS', max_length=1000, null=True)),
                ('trivia', models.TextField(help_text='Any related facts or trivia relating to this article', max_length=1000, null=True, blank=True)),
                ('youtubeid', models.CharField(help_text='Unique youtube video id for the trailer <a href="https://www.isbn-international.org/content/what-isbn">Youtube ID</a>', max_length=40, null=True, verbose_name='Youtube ID', blank=True)),
                ('actor', models.ManyToManyField(help_text='Select an actor for this article', to='catalog.Actor')),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('character', models.CharField(max_length=255)),
                ('actor', models.ForeignKey(related_name='films', to='catalog.Actor')),
                ('article', models.ForeignKey(related_name='actors', to='catalog.Article')),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField(null=True, blank=True)),
                ('date_of_death', models.DateField(null=True, verbose_name='Died', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Enter a article genre (e.g. Science Fiction, Action, Drama etc.)', max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='director',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='catalog.Director', null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='genre',
            field=models.ManyToManyField(help_text='Select a genre for this article', to='catalog.Genre'),
        ),
    ]
