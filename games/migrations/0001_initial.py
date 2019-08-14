# Generated by Django 2.1.8 on 2019-05-29 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('start_time', models.DateTimeField()),
                ('away_team', models.ForeignKey(db_column='away_team', on_delete=django.db.models.deletion.CASCADE, related_name='Game_Away_Team', to='team.Team')),
                ('home_team', models.ForeignKey(db_column='home_team', on_delete=django.db.models.deletion.CASCADE, related_name='Game_Home_Team', to='team.Team')),
            ],
            options={
                'db_table': 'Game',
            },
        ),
    ]
