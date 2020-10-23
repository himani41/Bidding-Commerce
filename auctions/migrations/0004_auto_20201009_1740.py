# Generated by Django 3.1 on 2020-10-09 12:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auto_20200926_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='value_offer',
            field=models.DecimalField(decimal_places=2, help_text='How much are you willing to pay for this item?', max_digits=8),
        ),
        migrations.AlterField(
            model_name='listing',
            name='bid',
            field=models.DecimalField(decimal_places=2, help_text='Starting bid (required), greater than 0 but less than $9,999,999', max_digits=10),
        ),
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(help_text='(not required) but this could help your product gain the spotlight it deserves! Examples of categories include Fashion, Toys, Electronics, Home, etc.', max_length=64),
        ),
        migrations.AlterField(
            model_name='listing',
            name='description',
            field=models.CharField(help_text="Description(required), Lets users know more about what you're selling! ", max_length=2048),
        ),
        migrations.AlterField(
            model_name='listing',
            name='image_url',
            field=models.CharField(help_text='(not required) but if you want to include an image for your product, please include an online url for it here!', max_length=2048),
        ),
        migrations.AlterField(
            model_name='listing',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owned_listings', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='listing',
            name='title',
            field=models.CharField(help_text='Title(required), Maximum 70 characters', max_length=64),
        ),
    ]