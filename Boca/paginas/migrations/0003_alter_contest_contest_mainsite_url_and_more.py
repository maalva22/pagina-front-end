# Generated by Django 4.0.3 on 2022-04-12 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0002_rename_contestl_contest_contest_main_site_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest',
            name='Contest_mainsite_URL',
            field=models.CharField(default='IP', max_length=200),
        ),
        migrations.AlterField(
            model_name='contest',
            name='Duration',
            field=models.IntegerField(default='in minutes'),
        ),
        migrations.AlterField(
            model_name='contest',
            name='Max_file_size_allowed_for_teams',
            field=models.IntegerField(default='in KB'),
        ),
        migrations.AlterField(
            model_name='contest',
            name='Penalty',
            field=models.IntegerField(default='in minutes'),
        ),
        migrations.AlterField(
            model_name='contest',
            name='Stop_Answering',
            field=models.IntegerField(default='in minutes'),
        ),
        migrations.AlterField(
            model_name='contest',
            name='Stop_Scoreboard',
            field=models.IntegerField(default='in minutes'),
        ),
    ]