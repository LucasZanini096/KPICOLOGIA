# Generated by Django 5.1.1 on 2024-11-08 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_consulta_dia_semana'),
    ]

    operations = [
        migrations.RenameField(
            model_name='consulta',
            old_name='repeticao',
            new_name='quinzenal',
        ),
        migrations.AddField(
            model_name='consulta',
            name='semanal',
            field=models.CharField(default=1, max_length=32),
            preserve_default=False,
        ),
    ]
