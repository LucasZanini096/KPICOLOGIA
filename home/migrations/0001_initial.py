<<<<<<< HEAD
# Generated by Django 5.1 on 2024-11-07 22:52
=======
# Generated by Django 5.1.1 on 2024-11-07 00:04
>>>>>>> 49db458a0f54c818457f4d7c2d202df4e5802c88

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AgendaPsico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia_semana', models.CharField(max_length=100)),
                ('hora', models.TimeField()),
                ('livre_ocupado', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Disponibilidade',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dia_semana', models.CharField(max_length=100)),
                ('hora', models.TimeField()),
                ('livre_ocupado', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('idade', models.IntegerField()),
                ('rg', models.IntegerField()),
                ('email', models.EmailField(max_length=100)),
                ('telefone', models.IntegerField()),
                ('cpf', models.IntegerField()),
                ('periodo', models.CharField(default='semanal', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Psicologa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=32)),
                ('tempo_consulta', models.DurationField(help_text='Duração de cada consulta (ex: 00:30:00 para 30 minutos)')),
                ('consultas_por_dia', models.PositiveIntegerField(help_text='Número máximo de consultas por dia')),
                ('horario_inicio', models.TimeField(help_text='Horário de início das consultas (ex: 09:00)')),
                ('cor', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Psicologo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=32)),
                ('cor', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id_sala', models.AutoField(primary_key=True, serialize=False)),
                ('cor_sala', models.CharField(choices=[('red', 'Vermelho'), ('green', 'Verde'), ('blue', 'Azul'), ('black', 'Preto'), ('white', 'Branco'), ('gray', 'Cinza'), ('yellow', 'Amarelo'), ('cyan', 'Ciano'), ('magenta', 'Magenta')], default='white', max_length=20)),
                ('numero_sala', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Unidade',
            fields=[
                ('id_unidade', models.AutoField(primary_key=True, serialize=False)),
                ('nome_unidade', models.CharField(max_length=100)),
                ('endereco_unidade', models.CharField(max_length=100)),
                ('CEP_unidade', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('idade', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('cargo', models.CharField(max_length=100)),
                ('telefone', models.IntegerField()),
                ('rg', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='PsicoDisponibilidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disponibilidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.agendapsico')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.psicologa')),
            ],
        ),
        migrations.CreateModel(
            name='ConfirmacaoConsulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField()),
                ('confirmacao', models.CharField(max_length=100)),
                ('forma_pagamento', models.CharField(max_length=100)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('observacoes', models.CharField(max_length=100)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.paciente')),
                ('psicologo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.psicologo')),
            ],
        ),
<<<<<<< HEAD
        migrations.CreateModel(
            name='PsicoConfirmarConsulta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('confirmacao_consulta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.confirmacaoconsulta')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PsicoDisponibilidade',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('disponibilidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.disponibilidade')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
=======
        migrations.AddField(
            model_name='sala',
            name='id_unidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salas', to='home.unidade'),
>>>>>>> 49db458a0f54c818457f4d7c2d202df4e5802c88
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario', models.DateTimeField()),
                ('repeticao', models.CharField(max_length=32)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.paciente')),
                ('psicologo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.psicologo')),
                ('sala', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.sala')),
            ],
        ),
        migrations.AddField(
            model_name='sala',
            name='id_unidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salas', to='home.unidade'),
        ),
    ]
