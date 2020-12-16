# Generated by Django 2.2.15 on 2020-09-04 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('picture', models.ImageField(upload_to='pictures')),
            ],
            options={
                'db_table': 'profile',
            },
        ),
        migrations.DeleteModel(
            name='Document',
        ),
    ]
