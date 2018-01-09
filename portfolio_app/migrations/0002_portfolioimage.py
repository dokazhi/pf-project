# Generated by Django 2.0.1 on 2018-01-09 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='C:\\Users\\dos\\dev\\portfolio_env\\pf_project\\media')),
                ('portfolio', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='image', to='portfolio_app.Portfolio')),
            ],
        ),
    ]
