# Generated by Django 4.2.1 on 2023-06-02 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_problem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=150)),
                ('comment', models.CharField(max_length=500, null=True)),
                ('goal_achieved', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
