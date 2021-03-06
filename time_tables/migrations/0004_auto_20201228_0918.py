# Generated by Django 3.1.4 on 2020-12-28 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('time_tables', '0003_auto_20201228_0827'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='name',
        ),
        migrations.AddField(
            model_name='subject',
            name='subject_name',
            field=models.CharField(choices=[('MATH', 'MATH'), ('ENGLISH', 'ENGLISH'), ('HISTORY', 'HISTORY')], default='MATH', help_text='과목', max_length=30),
        ),
        migrations.AlterField(
            model_name='timetablerecord',
            name='day_of_week',
            field=models.CharField(choices=[('MON', 'MON'), ('TUE', 'TUE'), ('WED', 'WED'), ('THU', 'THU'), ('FRI', 'FRI')], default='MON', help_text='요일', max_length=30),
        ),
    ]
