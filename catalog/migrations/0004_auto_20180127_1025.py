# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20180127_1009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='date_of_death',
        ),
        migrations.AddField(
            model_name='author',
            name='bio',
            field=models.TextField(help_text='Enter a brief description ', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='video_id',
            field=models.CharField(help_text='Unique youtube video id for the trailer <a href="https://www.isbn-international.org/content/what-isbn">Youtube ID</a>', max_length=1000, null=True, verbose_name='Video URL', blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='youtubeid',
            field=models.CharField(help_text='Unique youtube video id for the trailer <a href="https://www.isbn-international.org/content/what-isbn">Youtube ID</a>', max_length=1000, null=True, verbose_name='Youtube ID', blank=True),
        ),
    ]
