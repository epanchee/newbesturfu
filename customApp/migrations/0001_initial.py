# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20150824_2224'),
    ]

    operations = [
        migrations.CreateModel(
            name='DownloadedPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pages.Page')),
                ('dlink', models.TextField(verbose_name='\u0410\u0434\u0440\u0435\u0441 \u0441\u043a\u0430\u0447\u0438\u0432\u0430\u043d\u0438\u044f')),
                ('dlink_ru', models.TextField(null=True, verbose_name='\u0410\u0434\u0440\u0435\u0441 \u0441\u043a\u0430\u0447\u0438\u0432\u0430\u043d\u0438\u044f')),
                ('dlink_en', models.TextField(null=True, verbose_name='\u0410\u0434\u0440\u0435\u0441 \u0441\u043a\u0430\u0447\u0438\u0432\u0430\u043d\u0438\u044f')),
            ],
            options={
                'ordering': ('_order',),
            },
            bases=('pages.page',),
        ),
    ]
