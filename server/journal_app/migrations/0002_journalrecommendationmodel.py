# Generated by Django 4.1.1 on 2022-09-18 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JournalRecommendationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=40)),
                ('file', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'Journal_RecommendationModel',
            },
        ),
    ]
