# Generated by Django 3.2.7 on 2021-09-29 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Equipe',
            new_name='Funcionario',
        ),
        migrations.RenameField(
            model_name='servico',
            old_name='icon',
            new_name='icone',
        ),
    ]
