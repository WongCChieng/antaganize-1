# Generated by Django 4.0.3 on 2022-04-12 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('antaganize', '0003_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='source_img',
        ),
        migrations.AddField(
            model_name='image',
            name='image',
            field=models.ImageField(default=None, upload_to='images'),
            preserve_default=False,
        ),
    ]