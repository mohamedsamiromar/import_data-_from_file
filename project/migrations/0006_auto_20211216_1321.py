# Generated by Django 3.2.9 on 2021-12-16 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_alter_readupdate_attachment_links'),
    ]

    operations = [
        migrations.AddField(
            model_name='readupdate',
            name='s3',
            field=models.CharField(max_length=3072, null=True),
        ),
        migrations.AddField(
            model_name='readupdate',
            name='s3_1',
            field=models.CharField(max_length=3072, null=True),
        ),
    ]