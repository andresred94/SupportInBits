# Generated by Django 4.2.20 on 2025-04-03 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_remove_page_estilo_page_m_conten_page_m_http_equiv_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='descri',
            new_name='m_descri',
        ),
        migrations.RenameField(
            model_name='page',
            old_name='m_conten',
            new_name='m_handF',
        ),
        migrations.RenameField(
            model_name='page',
            old_name='m_http_equiv',
            new_name='m_mobileOp',
        ),
        migrations.AlterField(
            model_name='page',
            name='m_robots',
            field=models.CharField(max_length=255),
        ),
    ]
