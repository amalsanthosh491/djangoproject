# Generated by Django 4.1.5 on 2023-02-02 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app15', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=10)),
                ('Age', models.IntegerField()),
                ('Place', models.CharField(max_length=20)),
                ('Photo', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('Email', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=8)),
            ],
        ),
    ]
