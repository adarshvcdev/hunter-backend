# Generated by Django 2.1.2 on 2018-10-06 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bounce', '0002_auto_20181006_1233'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scrip',
            options={'ordering': ('ticker',)},
        ),
        migrations.AlterField(
            model_name='scrip',
            name='index',
            field=models.CharField(choices=[('Nifty', 'Nifty'), ('Midcap', 'Midcap'), ('Smallcap', 'Smallcap')], default='Nifty', max_length=100),
        ),
    ]
