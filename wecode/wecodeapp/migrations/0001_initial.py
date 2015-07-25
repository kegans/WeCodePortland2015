# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('question1', models.TextField()),
                ('question2', models.TextField()),
                ('question3', models.TextField()),
                ('question4', models.TextField()),
                ('pic', models.ImageField(default=b'pic_folder/None/no-img.jpg', upload_to=b'pic_folder/')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
