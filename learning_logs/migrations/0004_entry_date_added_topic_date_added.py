# Generated by Django 4.2.1 on 2023-05-18 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("learning_logs", "0003_topic_owner_alter_topic_text"),
    ]

    operations = [
        migrations.AddField(
            model_name="entry",
            name="date_added",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="topic",
            name="date_added",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
