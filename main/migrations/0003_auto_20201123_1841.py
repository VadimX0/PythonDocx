# Generated by Django 3.1.3 on 2020-11-23 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_chkbx_doc'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='chkbx',
            new_name='chkboxcourse',
        ),
        migrations.RenameField(
            model_name='chkboxcourse',
            old_name='coursname',
            new_name='coursename',
        ),
    ]
