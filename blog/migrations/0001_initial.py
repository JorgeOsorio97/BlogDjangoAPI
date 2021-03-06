# Generated by Django 3.0.6 on 2020-05-28 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_publ', models.DateTimeField(auto_created=True)),
                ('titulo', models.TextField(max_length=150)),
                ('imagen', models.ImageField(upload_to='media/')),
                ('texto_intro', models.TextField(max_length=250)),
                ('texto_completo', models.TextField()),
            ],
        ),
    ]
