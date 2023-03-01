# Generated by Django 4.1.6 on 2023-03-01 16:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(default='default.jpg', upload_to='media/')),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('followers', models.IntegerField(blank=True, null=True)),
                ('following', models.IntegerField(blank=True, null=True)),
                ('bio', models.TextField(blank=True, max_length=200)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=300)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('replycount', models.IntegerField(default=0)),
                ('likes', models.ManyToManyField(related_name='tweet_likes', to='twitter.profile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='twitter.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, max_length=200, null=True)),
                ('like', models.IntegerField(blank=True, default=0, null=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('commenter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='twitter.profile')),
                ('tweet', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='twitter.tweet')),
            ],
        ),
    ]