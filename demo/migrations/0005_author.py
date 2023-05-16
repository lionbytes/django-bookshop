# Generated by Django 4.0.2 on 2023-05-16 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0004_character'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
                ('books', models.ManyToManyField(related_name='authors', to='demo.Book')),
            ],
        ),
    ]