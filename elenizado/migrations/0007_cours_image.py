# Generated by Django 2.2.12 on 2020-06-29 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elenizado', '0006_remove_evenement_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='cours',
            name='image',
            field=models.ImageField(default='cours/pdf.png', upload_to='cours/image'),
        ),
    ]
