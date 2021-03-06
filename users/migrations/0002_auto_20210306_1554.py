# Generated by Django 3.1.6 on 2021-03-06 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photoshare/media')),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('description_field', models.CharField(max_length=150, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='commented_image',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='fname',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='lname',
        ),
        migrations.AddField(
            model_name='comment',
            name='cuser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
        migrations.AddField(
            model_name='comment',
            name='description_field',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.AddField(
            model_name='post',
            name='puser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
    ]
