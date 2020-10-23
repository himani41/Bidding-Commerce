# Generated by Django 3.1 on 2020-10-13 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_remove_comment_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(blank=True, help_text='This could help your product gain the spotlight it deserves! Examples of categories include Fashion, Toys, Electronics, Home, etc.', max_length=64),
        ),
        migrations.AlterField(
            model_name='listing',
            name='image_url',
            field=models.CharField(blank=True, help_text='(not required) but if you want to include an image for your product, please include an online url for it here!', max_length=2048),
        ),
    ]
