# Generated by Django 4.0.1 on 2022-04-09 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grievance_data', '0010_alter_category_cat_name_alter_grievance_gri_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grievance',
            name='gri_img',
            field=models.ImageField(upload_to='grievance_pics'),
        ),
    ]
