
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shrt_my_link', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Links',
            new_name='Link',
        ),
    ]
