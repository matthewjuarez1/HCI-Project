# Generated by Django 4.1.3 on 2022-12-05 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_poem_contents_compilation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compilation',
            name='anthologies',
        ),
        migrations.RemoveField(
            model_name='compilation',
            name='books',
        ),
        migrations.RemoveField(
            model_name='compilation',
            name='chapters',
        ),
        migrations.RemoveField(
            model_name='compilation',
            name='characters',
        ),
        migrations.RemoveField(
            model_name='compilation',
            name='ideas',
        ),
        migrations.RemoveField(
            model_name='compilation',
            name='media',
        ),
        migrations.RemoveField(
            model_name='compilation',
            name='poems',
        ),
        migrations.RemoveField(
            model_name='compilation',
            name='series',
        ),
        migrations.RemoveField(
            model_name='compilation',
            name='themes',
        ),
        migrations.AddField(
            model_name='compilation',
            name='anthologies',
            field=models.ManyToManyField(to='main.anthology'),
        ),
        migrations.AddField(
            model_name='compilation',
            name='books',
            field=models.ManyToManyField(to='main.book'),
        ),
        migrations.AddField(
            model_name='compilation',
            name='chapters',
            field=models.ManyToManyField(to='main.chapter'),
        ),
        migrations.AddField(
            model_name='compilation',
            name='characters',
            field=models.ManyToManyField(to='main.character'),
        ),
        migrations.AddField(
            model_name='compilation',
            name='ideas',
            field=models.ManyToManyField(to='main.idea'),
        ),
        migrations.AddField(
            model_name='compilation',
            name='media',
            field=models.ManyToManyField(to='main.media'),
        ),
        migrations.AddField(
            model_name='compilation',
            name='poems',
            field=models.ManyToManyField(to='main.poem'),
        ),
        migrations.AddField(
            model_name='compilation',
            name='series',
            field=models.ManyToManyField(to='main.series'),
        ),
        migrations.AddField(
            model_name='compilation',
            name='themes',
            field=models.ManyToManyField(to='main.theme'),
        ),
    ]