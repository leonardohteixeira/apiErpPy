# Generated by Django 4.2.4 on 2024-11-24 22:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0002_group_user_groups_group_permissions'),
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Entrerprise',
            new_name='Enterprise',
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enterprise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.enterprise')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
