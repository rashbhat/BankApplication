# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountDetails',
            fields=[
                ('account_id', models.AutoField(serialize=False, primary_key=True)),
                ('account_type', models.CharField(max_length=200)),
                ('account_balance', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BankDetails',
            fields=[
                ('bank_id', models.AutoField(serialize=False, primary_key=True)),
                ('bank_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TransactionDetails',
            fields=[
                ('trans_id', models.AutoField(serialize=False, primary_key=True)),
                ('trans_type', models.CharField(max_length=200)),
                ('trans_amount', models.IntegerField()),
                ('account_id', models.ForeignKey(to='BankApp.AccountDetails')),
            ],
        ),
        migrations.CreateModel(
            name='UserBankMap',
            fields=[
                ('userBankMap_id', models.AutoField(serialize=False, primary_key=True)),
                ('bank_id', models.ForeignKey(to='BankApp.BankDetails')),
            ],
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('user_id', models.AutoField(serialize=False, primary_key=True)),
                ('user_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='userbankmap',
            name='user_id',
            field=models.ForeignKey(to='BankApp.UserDetails'),
        ),
        migrations.AddField(
            model_name='accountdetails',
            name='userBankMap_id',
            field=models.ForeignKey(to='BankApp.UserBankMap'),
        ),
    ]
