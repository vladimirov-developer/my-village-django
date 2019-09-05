# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.translation


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Metadata',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url_path', models.CharField(max_length=255, verbose_name='URL path', db_index=True)),
                ('language', models.CharField(default=django.utils.translation.get_language, max_length=10, verbose_name='language', db_index=True, choices=[(b'ru', 'Russian')])),
                ('title', models.CharField(help_text='Displayed in browser window title.', max_length=255, verbose_name='page title', blank=True)),
                ('title_extend', models.BooleanField(default=True, help_text='For example, <strong>Page title - Site name</strong>', verbose_name='extend page title with site name')),
                ('keywords', models.TextField(help_text='Keywords are terms describing web page content and used by search engines. Here you can enumerate some words divided by commas.', verbose_name='page keywords', blank=True)),
                ('description', models.TextField(help_text='Here you can set short description of this page for search engines.', verbose_name='page description', blank=True)),
                ('priority', models.FloatField(default=0.5, help_text='The priority of this URL relative to other URLs on your site. Valid values range from 0.0 to 1.0. This value does not affect how your pages are compared to pages on other sites - it only lets the search engines know which pages you deem most important for the crawlers.<br /> More info you can read in <a href="http://www.sitemaps.org/protocol.php" target="_blank">Sitemap protocol description</a>.', null=True, verbose_name='page priority', blank=True)),
                ('changefreq', models.CharField(default=b'monthly', help_text='How frequently the page is likely to change. This value provides general information to search engines and may not correlate exactly to how often they crawl the page.<br /> The value <strong>always</strong> should be used to describe documents that change each time they are accessed. The value <strong>never</strong> should be used to describe archived URLs.<br /> More info you can read in <a href="http://www.sitemaps.org/protocol.php" target="_blank">Sitemap protocol description</a>.', max_length=7, verbose_name='page change frequency', choices=[(b'never', 'never'), (b'always', 'always'), (b'hourly', 'hourly'), (b'daily', 'daily'), (b'weekly', 'weekly'), (b'monthly', 'monthly'), (b'yearly', 'yearly')])),
                ('lastmod', models.DateTimeField(auto_now=True, verbose_name='last modification date', null=True)),
                ('enabled', models.BooleanField(default=True, help_text='If not set, meta tags will not be used on page.', verbose_name='enabled')),
                ('object_id', models.PositiveIntegerField(null=True, editable=False)),
                ('content_type', models.ForeignKey(editable=False, to='contenttypes.ContentType', null=True)),
                ('sites', models.ManyToManyField(related_name='+', null=True, verbose_name='sites', to='sites.Site', blank=True)),
            ],
            options={
                'verbose_name': 'page',
                'verbose_name_plural': 'pages',
            },
            bases=(models.Model,),
        ),
    ]
