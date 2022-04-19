# Generated by Django 3.2.12 on 2022-04-02 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.AddField(
            model_name='post',
            name='comment',
            field=models.ManyToManyField(to='blog.Comment'),
        ),
    ]
