# Generated by Django 3.1.1 on 2020-11-17 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GoodnessGroceries', '0016_auto_20201117_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cashierticketproducts',
            name='reviewed',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
