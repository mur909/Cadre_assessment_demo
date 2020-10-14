# Generated by Django 2.2 on 2020-08-07 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('others', '0005_auto_20200807_1225'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='roles',
        ),
        migrations.AddField(
            model_name='user',
            name='roles',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='others.Role', verbose_name='用户所拥有的角色'),
            preserve_default=False,
        ),
    ]
