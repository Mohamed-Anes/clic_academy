# Generated by Django 4.2.1 on 2023-07-06 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_exo4_table_conjugaison'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exo4',
            name='table_conjugaison',
        ),
        migrations.AddField(
            model_name='exo4',
            name='temps_conjugaison',
            field=models.CharField(choices=[('A', 'الماضي'), ('B', 'المضارع'), ('C', 'المضارع المنصوب'), ('D', 'الماضي المبني للمجهول'), ('E', 'المضارع المبني للمجهول'), ('F', 'المضارع المجزوم'), ('G', 'الأمر')], max_length=1, null=True),
        ),
    ]
