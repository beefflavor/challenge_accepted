# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0002_submissionv'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='challengev',
            name='mod_at',
        ),
    ]
