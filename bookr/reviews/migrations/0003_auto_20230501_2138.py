# Generated by Django 3.0a1 on 2023-05-01 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20191007_0112'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='book_covers/'),
        ),
        migrations.AddField(
            model_name='book',
            name='sample',
            field=models.FileField(blank=True, null=True, upload_to='book_samples/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.Publisher'),
        ),
        migrations.AlterField(
            model_name='review',
            name='date_edited',
            field=models.DateTimeField(help_text='The date and time the review was last edited.', null=True),
        ),
    ]
