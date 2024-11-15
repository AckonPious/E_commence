# Generated by Django 5.1.1 on 2024-09-13 14:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categroy',
            options={'ordering': ('name',), 'verbose_name_plural': 'Categroies'},
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.FloatField()),
                ('images', models.ImageField(blank=True, null=True, upload_to='Image_items')),
                ('is_sold', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('Categroy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='item.categroy')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
