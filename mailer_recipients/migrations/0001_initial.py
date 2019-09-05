# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('content_type', models.ForeignKey(verbose_name='content type', to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': 'recipient',
                'verbose_name_plural': 'recipients',
            },
        ),
    ]
