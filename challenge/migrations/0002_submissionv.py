# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('challenge', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submissionv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('video', models.URLField(max_length=255)),
                ('post_at', models.DateTimeField(auto_now_add=True)),
                ('mod_at', models.DateTimeField(auto_now=True)),
                ('challenge', models.ForeignKey(to='challenge.Challengev')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
