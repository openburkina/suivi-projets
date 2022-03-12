# Generated by Django 3.1.13 on 2022-02-11 17:53

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('undp_projects', '0008_projectindicator'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='planification_year',
        ),
        migrations.CreateModel(
            name='ProjectDec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dec_date', models.DateField(db_index=True, default=django.utils.timezone.now)),
                ('amount_dec', models.FloatField(blank=True, null=True)),
                ('deliverable', models.CharField(blank=True, max_length=600, null=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='undp_projects.project')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(db_index=True, default=django.utils.timezone.now)),
                ('finish_date', models.DateField(db_index=True, default=django.utils.timezone.now)),
                ('amount_act', models.FloatField(blank=True, null=True)),
                ('Actors_execution', models.CharField(blank=True, max_length=15, null=True)),
                ('Actors_partner', models.CharField(blank=True, max_length=15, null=True)),
                ('year_plan', models.IntegerField(blank=True, null=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='undp_projects.project')),
            ],
        ),
    ]