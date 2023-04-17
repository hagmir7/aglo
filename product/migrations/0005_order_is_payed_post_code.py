# Generated by Django 4.0.3 on 2023-04-16 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_contact_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_payed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='code',
            field=models.TextField(blank=True, null=True),
        ),
    ]