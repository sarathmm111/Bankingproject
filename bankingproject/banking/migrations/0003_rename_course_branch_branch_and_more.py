# Generated by Django 4.1.7 on 2023-03-04 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('banking', '0002_rename_course_branch_rename_department_district_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='branch',
            old_name='course',
            new_name='branch',
        ),
        migrations.RenameField(
            model_name='branch',
            old_name='deptid',
            new_name='distid',
        ),
        migrations.RenameField(
            model_name='district',
            old_name='departmentname',
            new_name='districtname',
        ),
    ]