# Generated by Django 3.0.3 on 2020-02-06 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RankingList',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False, verbose_name='序号')),
                ('cname', models.CharField(max_length=30, verbose_name='姓名')),
                ('cscore', models.IntegerField(default=0)),
            ],
        ),
    ]
