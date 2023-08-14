# Generated by Django 4.1.5 on 2023-08-06 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0004_delete_contagemorcamento_alter_orcamento_pag2"),
    ]

    operations = [
        migrations.AddField(
            model_name="cliente",
            name="medico",
            field=models.IntegerField(
                choices=[
                    (1, "Cristiano Dias da Silveira Ramos"),
                    (2, "Érika Lawall Lopoes Ramos"),
                ],
                default=0,
            ),
            preserve_default=False,
        ),
    ]