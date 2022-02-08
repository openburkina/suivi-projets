# Generated by Django 3.1.13 on 2022-01-22 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('undp_projects', '0004_remove_project_executant'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectTimeLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(db_index=True)),
                ('finish_date', models.DateField(db_index=True)),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='undp_projects.project')),
            ],
        ),
    ]
