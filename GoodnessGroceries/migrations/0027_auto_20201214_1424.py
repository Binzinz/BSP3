# Generated by Django 3.1.3 on 2020-12-14 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GoodnessGroceries', '0026_auto_20201214_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreviews',
            name='static_product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='GoodnessGroceries.staticproducts'),
        ),
    ]
