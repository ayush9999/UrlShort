
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shrt_my_link', '0002_auto_20170216_1655'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='link',
            name='count',
        ),
        migrations.AddField(
            model_name='link',
            name='clickCount',
            field=models.IntegerField(default=0),
        ),
    ]
