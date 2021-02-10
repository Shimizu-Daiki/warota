# Generated by Django 3.1.4 on 2021-02-10 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='回答者名\u3000')),
                ('text', models.TextField(max_length=100, verbose_name='回答を入力')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='登録日')),
            ],
            options={
                'verbose_name': '回答',
                'verbose_name_plural': '回答',
            },
        ),
        migrations.AlterField(
            model_name='problem',
            name='name',
            field=models.CharField(max_length=20, verbose_name='登録者名\u3000'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='text',
            field=models.TextField(max_length=100, verbose_name='お題を入力'),
        ),
    ]
