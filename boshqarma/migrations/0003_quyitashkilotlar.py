# Generated by Django 4.0.3 on 2022-07-13 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boshqarma', '0002_sendmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuyiTashkilotlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('info', models.TextField(null=True)),
                ('image', models.ImageField(upload_to='branches/')),
            ],
        ),
    ]
