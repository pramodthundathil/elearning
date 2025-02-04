# Generated by Django 5.0.6 on 2024-12-19 15:27

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0002_studymaterials_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studymaterials',
            name='category',
            field=models.CharField(choices=[('Assignment', 'Assignment'), ('Notes', 'Notes'), ('Others', 'Others'), ('Project Contents', 'Project Contents')], max_length=100),
        ),
        migrations.AlterField(
            model_name='studymaterials',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
