# Generated by Django 5.0.6 on 2024-12-20 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0003_alter_studymaterials_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='studymaterials',
            name='course',
            field=models.CharField(choices=[('B.Tech', 'B.Tech'), ('M.Tech', 'M.Tech'), ('MCA', 'MCA'), ('BCA', 'BCA'), ('MBA', 'MBA'), ('BBA', 'BBA'), ('B.Sc', 'B.Sc'), ('M.Sc', 'M.Sc'), ('B.Com', 'B.Com'), ('M.Com', 'M.Com'), ('B.A', 'B.A'), ('M.A', 'M.A')], default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studymaterials',
            name='stream',
            field=models.CharField(choices=[('Civil', 'Civil'), ('Taxation', 'Taxation'), ('AI', 'AI'), ('General', 'General'), ('Mechanical', 'Mechanical'), ('Electrical', 'Electrical'), ('Computer Science', 'Computer Science'), ('Electronics', 'Electronics'), ('Chemical', 'Chemical'), ('Biotechnology', 'Biotechnology')], default=1, max_length=100),
            preserve_default=False,
        ),
    ]
