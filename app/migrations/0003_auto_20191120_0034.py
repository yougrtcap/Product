# Generated by Django 2.2.7 on 2019-11-19 15:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('app', '0002_photo_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to='photos'),
        ),
    ]