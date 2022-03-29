import imp
from turtle import title
from django.db import models
from django.forms import CharField
from django.urls import reverse



# Create your models here.


'''
14.03 - разобраться с загрузкой нескольких фото
 и связями по категориям, размеру
 + заменить базу данных на postgres

 узнать как поставить валидатор на минимальное значение пол] Price
 узнать как сделать множество размеров для одного продукта

   id
 title = charfield
 description = textfield
 category = charfield +
 price = IntegerField
 color = CharField
 size = CharField
 brand = CharField
 image = ImageField +
 is_available = bool
 
'''

class Product(models.Model):

    title = models.CharField(max_length=100, verbose_name='Product name')
    descriptioin = models.TextField(verbose_name='Product descritption')
    price = models.IntegerField(verbose_name='Price')
    color = models.ForeignKey('Color', on_delete=models.CASCADE)
    size = models.CharField(max_length=100, blank=True, verbose_name='Sizes')
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True, verbose_name='Available')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product-photos/%Y/%m/%d/')
    slug = models.SlugField(max_length=100, verbose_name='Url', unique=True, default=None)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product', kwargs={"slug": self.slug})

class Category(models.Model):
    title = models.CharField(max_length=40, db_index=True, verbose_name='Category')
    slug = models.SlugField(max_length=40, verbose_name='Url', unique=True, default=None)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={"slug": self.slug})

    class Meta:
        verbose_name_plural = 'Categories'


class Color(models.Model):
    title = models.CharField(max_length=20, db_index=True, verbose_name='Color')
    slug = models.SlugField(max_length=20, verbose_name='Url', unique=True, default=None)
    color_code = models.CharField(max_length=7, default='#000000', verbose_name='Color Code')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('color', kwargs={"slug": self.slug})

class Brand(models.Model):
    title = models.CharField(max_length=45, db_index=True, verbose_name='Brand')
    slug = models.SlugField(max_length=45, verbose_name='Url', unique=True, default=None)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('brand', kwargs={"slug": self.slug})

# '''

#class SubCategories(models.Model):
#    Category = models.ForeignKey(Category)
#    SubCategory = models.CharField()
# admin, 3ac


''''
class Size_table(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.PROTECT)
    size = models.CharField(max_length=5, verbose_name='Size')
    size_number = models.IntegerField(verbose_name='Size number')
    count = models.IntegerField(verbose_name='Product count with this size')

SELECT title, size, size_number, count
FROM product JOIN size_table
    ON product.primary_key = size_table.product_id
JOIN size_count ON size_table.primary_key = size_count.size_id
'''