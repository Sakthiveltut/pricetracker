# Generated by Django 4.1.7 on 2023-04-14 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_delete_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aproducts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.aproducts')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category')),
                ('fproducts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.fproducts')),
            ],
        ),
    ]
