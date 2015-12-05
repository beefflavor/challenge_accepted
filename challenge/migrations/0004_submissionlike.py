# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('challenge', '0003_remove_challengev_mod_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubmissionLike',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('post_at', models.DateTimeField(auto_now_add=True)),
                ('mod_at', models.DateTimeField(auto_now=True)),
                ('like', models.ForeignKey(to='challenge.Submissionv')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
