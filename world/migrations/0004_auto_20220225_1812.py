# Generated by Django 3.2 on 2022-02-25 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0003_auto_20220222_0825'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='uncategorized', max_length=255),
        ),
    ]