# Generated by Django 2.0.5 on 2018-05-09 19:32

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sourcebook_app', '0006_auto_20180509_1922'),
    ]

    operations = [
        migrations.CreateModel(
            name='subcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('essay', ckeditor.fields.RichTextField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='subcategory',
            field=models.ManyToManyField(blank=True, to='sourcebook_app.subcategory'),
        ),
    ]
