# Generated by Django 3.2.12 on 2024-04-12 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MangoliciousApp', '0003_remove_details_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='RipeMangoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ahmedabad', models.IntegerField()),
                ('Rajkot', models.IntegerField()),
                ('Mumbai', models.IntegerField()),
                ('Jamnagar', models.IntegerField()),
                ('Khambhaliya', models.IntegerField()),
                ('Surat', models.IntegerField()),
                ('Baroda', models.IntegerField()),
                ('Junagadh', models.IntegerField()),
                ('SavarKundla', models.IntegerField()),
                ('Viramgam', models.IntegerField()),
                ('Wankaner', models.IntegerField()),
                ('Amreli', models.IntegerField()),
                ('Gondal', models.IntegerField()),
                ('Jetpur', models.IntegerField()),
                ('Porbandar', models.IntegerField()),
                ('Bhavnagar', models.IntegerField()),
                ('Veraval', models.IntegerField()),
                ('Talala_Gir', models.IntegerField()),
                ('Una', models.IntegerField()),
                ('Kodinar', models.IntegerField()),
                ('Dwarka', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('quantityIn', models.CharField(max_length=200)),
            ],
        ),
    ]
