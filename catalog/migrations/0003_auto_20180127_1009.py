# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20180127_0810'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Director',
            new_name='Author',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='director',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='trivia',
            new_name='summary_four',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='poster',
            new_name='summary_one',
        ),
        migrations.RemoveField(
            model_name='article',
            name='actor',
        ),
        migrations.RemoveField(
            model_name='article',
            name='summary',
        ),
        migrations.AddField(
            model_name='article',
            name='poster_four',
            field=models.CharField(help_text='Enter a URL to the main image of the article', max_length=1000, null=True, verbose_name='Image URL 1'),
        ),
        migrations.AddField(
            model_name='article',
            name='poster_one',
            field=models.CharField(help_text='Enter a URL to the main image of the article', max_length=1000, null=True, verbose_name='Image URL 1'),
        ),
        migrations.AddField(
            model_name='article',
            name='poster_three',
            field=models.CharField(help_text='Enter a URL to the main image of the article', max_length=1000, null=True, verbose_name='Image URL 1'),
        ),
        migrations.AddField(
            model_name='article',
            name='poster_two',
            field=models.CharField(help_text='Enter a URL to the main image of the article', max_length=1000, null=True, verbose_name='Image URL 1'),
        ),
        migrations.AddField(
            model_name='article',
            name='summary_three',
            field=models.TextField(help_text='Any related facts or trivia relating to this article', max_length=1000, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='summary_two',
            field=models.TextField(help_text='Any related facts or trivia relating to this article', max_length=1000, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='video_id',
            field=models.CharField(help_text='Unique youtube video id for the trailer <a href="https://www.isbn-international.org/content/what-isbn">Youtube ID</a>', max_length=40, null=True, verbose_name='Youtube ID', blank=True),
        ),
    ]
