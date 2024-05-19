# Generated by Django 4.2.11 on 2024-05-19 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='useraddress',
            name='unique_primary_per_user',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='profiles.useraddress'),
        ),
    ]
