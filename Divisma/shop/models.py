from email.policy import default
import imp
from turtle import title
from unicodedata import category
from django.db import models
from django.forms import CharField
from django.urls import reverse
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill



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
    title = models.CharField(max_length=100, verbose_name='Product name', default='Product name')
    description = models.TextField(verbose_name='Product descritption', default = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin pharetra tempor so dales. Phasellus sagittis auctor gravida. Integer bibendum sodales arcu id te mpus. Ut consectetur lacus leo, non scelerisque nulla euismod nec. Approx length 66cm/26 (Based on a UK size 8 sample) Mixed fibres The Model wears a UK size 8/ EU size 36/ US size 4 and her height is 5.8')
    price = models.IntegerField(verbose_name='Price')
    is_available = models.BooleanField(default=True, verbose_name='Available')
    is_OnSale = models.BooleanField(default=False, verbose_name='On sale')
    slug = models.SlugField(max_length=100, verbose_name='Url', unique=True, default=None)

    #filter fields
    color = models.ForeignKey('Color', on_delete=models.DO_NOTHING)
    size = models.ManyToManyField('Size')
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    sub_category = models.ForeignKey('shop.SubCategory', on_delete=models.DO_NOTHING, default=1)

    #source images which you loading
    image = models.ImageField(upload_to='product-photos/%Y/%m/%d/', default='product-photos/default.jpg')
    image1 = models.ImageField(upload_to='product-photos/%Y/%m/%d/', default='product-photos/default.jpg')
    image2 = models.ImageField(upload_to='product-photos/%Y/%m/%d/', default='product-photos/default.jpg')
    image3 = models.ImageField(upload_to='product-photos/%Y/%m/%d/', default='product-photos/default.jpg')
    
    #core image which display in shop
    image_core = ImageSpecField(source='image',
                                        processors=[ResizeToFill(500,775)],
                                        format='JPEG',
                                        options={'quality': 100})
    
    #images which displayed on single product page
    image_resize = ImageSpecField(source='image',
                                        processors=[ResizeToFill(1000,1358)],
                                        format='JPEG',
                                        options={'quality': 100})
    image1_resize = ImageSpecField(source='image1',
                                        processors=[ResizeToFill(1000,1358)],
                                        format='JPEG',
                                        options={'quality': 100})
    image2_resize = ImageSpecField(source='image2',
                                        processors=[ResizeToFill(1000,1358)],
                                        format='JPEG',
                                        options={'quality': 100})
    image3_resize = ImageSpecField(source='image3',
                                        processors=[ResizeToFill(1000,1358)],
                                        format='JPEG',
                                        options={'quality': 100})
    #and their thumbs
    thumb_image = ImageSpecField(source='image',
                                        processors=[ResizeToFill(116,116)],
                                        format='JPEG',
                                        options={'quality': 80})
    thumb_image1 = ImageSpecField(source='image1',
                                        processors=[ResizeToFill(116,116)],
                                        format='JPEG',
                                        options={'quality': 80})
    thumb_image2 = ImageSpecField(source='image2',
                                        processors=[ResizeToFill(116,116)],
                                        format='JPEG',
                                        options={'quality': 80})
    thumb_image3 = ImageSpecField(source='image3',
                                        processors=[ResizeToFill(116,116)],
                                        format='JPEG',
                                        options={'quality': 80})

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product', kwargs={"slug": self.slug})


class Size(models.Model):
    title = models.CharField(max_length=40, db_index=True, verbose_name='Size')
    slug = models.SlugField(max_length=40, verbose_name='Url', unique=True, default=None)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('size', kwargs={"slug": self.slug})

    class Meta:
        verbose_name_plural = 'Sizes'


class Category(models.Model):
    title = models.CharField(max_length=40, db_index=True, verbose_name='Category')
    slug = models.SlugField(max_length=40, verbose_name='Url', unique=True, default=None)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={"slug": self.slug})

    class Meta:
        verbose_name_plural = 'Categories'

class SubCategory(models.Model):
    title = models.CharField(max_length=40, db_index=True, verbose_name='Sub Category')
    category = models.ForeignKey('Category', on_delete=models.DO_NOTHING)
    slug = models.SlugField(max_length=40, verbose_name='Url', unique=True, default=None)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('sub_category', kwargs={"slug": self.slug})

    class Meta:
        verbose_name_plural = 'Sub categories'


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