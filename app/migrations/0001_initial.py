# Generated by Django 5.0.6 on 2024-08-16 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Images/students')),
                ('name', models.CharField(max_length=50)),
                ('direction', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Images/courses')),
                ('money', models.DecimalField(decimal_places=2, max_digits=10)),
                ('type', models.CharField(max_length=50)),
                ('teacher', models.CharField(max_length=50)),
                ('time', models.IntegerField()),
                ('students', models.IntegerField()),
                ('rating', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Instructors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Images/instructors')),
                ('name', models.CharField(max_length=50)),
                ('director', models.CharField(max_length=50)),
            ],
        ),
    ]