# Generated by Django 5.1.1 on 2024-10-06 23:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financeapp', '0006_categories_transactiontypes_transactions'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Categories',
        ),
        migrations.DeleteModel(
            name='Transactions',
        ),
        migrations.DeleteModel(
            name='TransactionTypes',
        ),
    ]
