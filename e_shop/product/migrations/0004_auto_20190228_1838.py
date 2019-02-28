# Generated by Django 2.1.7 on 2019-02-28 18:38

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20190226_1608'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('category', models.ForeignKey(on_delete='Cascade', related_name='producer_category', to='product.Category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Производитель',
                'verbose_name_plural': 'Производители',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='sale',
            field=models.BooleanField(default=False, verbose_name='Товар по акции?'),
        ),
        migrations.AddField(
            model_name='product',
            name='sale_precent',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Процент скидки'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete='Cascade', related_name='product_category', to='product.Category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='product',
            name='producer',
            field=models.ForeignKey(default=1, on_delete='Cascade', related_name='product_producer', to='product.Producer', verbose_name='Производитель'),
            preserve_default=False,
        ),
    ]