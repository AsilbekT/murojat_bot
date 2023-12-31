# Generated by Django 4.2.5 on 2023-09-12 21:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('botapp', '0003_category_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contents', to='botapp.category'),
        ),
        migrations.AlterField(
            model_name='content',
            name='file',
            field=models.FileField(upload_to='tutorials/'),
        ),
        migrations.AlterField(
            model_name='content',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
