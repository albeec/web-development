# Generated by Django 2.2 on 2020-05-20 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200508_0045'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['-publish_date', '-updated', '-timestamp']},
        ),
        migrations.RenameField(
            model_name='blogpost',
            old_name='publishe_date',
            new_name='publish_date',
        ),
    ]
