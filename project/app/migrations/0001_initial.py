# Generated by Django 5.1.5 on 2025-01-16 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(db_index=True, help_text='Enter a unique username', max_length=30, null=True, unique=True)),
                ('email', models.EmailField(db_index=True, max_length=255, unique=True)),
                ('bio', models.CharField(blank=True, db_index=True, help_text='Write a short bio about yourself', max_length=50, null=True)),
                ('is_active', models.BooleanField(db_index=True, default=False)),
                ('Qualification', models.CharField(choices=[('b,tech', 'b-tech'), ('m,tech', 'm-tech'), ('b.sc', 'b-sc')], db_index=True, max_length=100, null=True, verbose_name='Quali')),
            ],
        ),
    ]
