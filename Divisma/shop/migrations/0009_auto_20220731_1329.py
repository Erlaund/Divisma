# Generated by Django 3.2.12 on 2022-07-31 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_rename_descriptioin_product_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=40, verbose_name='Size')),
                ('slug', models.SlugField(default=None, max_length=40, unique=True, verbose_name='Url')),
            ],
            options={
                'verbose_name_plural': 'Sizes',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='is_OnSale',
            field=models.BooleanField(default=False, verbose_name='On sale'),
        ),
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shop.color'),
        ),
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.ManyToManyField(to='shop.Size'),
        ),
    ]
