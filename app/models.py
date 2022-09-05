from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profile_pic = CloudinaryField('image', null=True, blank=True)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, null=True, blank=True)

    @property
    def get_name(self):
        return self.user.username


class Category_One(models.Model):
    CATEGORIES = (
        ('Todays_Deals', 'Todays_Deals'),
        ('Recommended', 'Recommended'),
        ('Similar', 'Similar'),
    )
    name = models.CharField(max_length=50, choices=CATEGORIES)

    def __str__(self):
        return self.name


class Category_Two(models.Model):
    CATEGORIES = (
        ('Health_Beauty', 'Health_Beauty'),
        ('Kitchen_Appliances', 'Kitchen_Appliances'),
        ('Phone_Tablets', 'Phone_Tablets'),
        ('Electronics', 'Electronics'),
        ('Fashion', 'Fashion'),
        ('Garden_Outdoors', 'Garden_Outdoors'),
        ('Furniture', 'Furniture'),
    )
    name = models.CharField(max_length=50, choices=CATEGORIES)

    def __str__(self):
        return self.name


# class Today_Deals(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
#     name = models.CharField(max_length=100)
#     brand = models.CharField(max_length=100)
#     description = models.CharField(max_length=500)
#     new_price = models.CharField(max_length=20)
#     old_price = models.CharField(max_length=20, blank=True)
#     profile_pic = CloudinaryField('image', null=True, blank=True)
#     category = models.ForeignKey(Category,on_delete=models.CASCADE,default='')

#     def __str__(self):
#         return self.name


# class Recommended_Products(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
#     name = models.CharField(max_length=100)
#     brand = models.CharField(max_length=100)
#     description = models.CharField(max_length=500)
#     new_price = models.CharField(max_length=20)
#     old_price = models.CharField(max_length=20, blank=True)
#     profile_pic = CloudinaryField('image', null=True, blank=True)
#     category = models.ForeignKey(Category,on_delete=models.CASCADE,default='')

#     def __str__(self):
#         return self.name


class Products(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    new_price = models.CharField(max_length=20)
    old_price = models.CharField(max_length=20, blank=True)
    image = CloudinaryField('product_image', null=True, blank=True)
    category_one = models.ForeignKey(
        Category_One, on_delete=models.CASCADE, null=True)
    category_two = models.ForeignKey(
        Category_Two, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    @classmethod
    def filter_by_category1(cls, category_one):
        product_category1 = Products.objects.filter(
            category1__name=category_one).all()
        return product_category1

    @classmethod
    def filter_by_category2(cls, category_two):
        product_category2 = Products.objects.filter(
            category1__name=category_two).all()
        return product_category2


# class Similar_Products(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
#     name = models.CharField(max_length=100)
#     brand = models.CharField(max_length=100)
#     description = models.CharField(max_length=500)
#     new_price = models.CharField(max_length=20)
#     old_price = models.CharField(max_length=20, blank=True)
#     profile_pic = CloudinaryField('image', null=True, blank=True)
#     category = models.ForeignKey(Category,on_delete=models.CASCADE,default='')

#     def __str__(self):
#         return self.name


class Orders(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Order Confirmed', 'Order Confirmed'),
        ('Out for Delivery', 'Out for Delivery'),
        ('Delivered', 'Delivered'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    products = models.ForeignKey(
        'Products', on_delete=models.CASCADE, null=True, blank=True)
    email = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=500, null=True)
    phone = models.CharField(max_length=20, null=True)
    order_date = models.DateField(auto_now_add=True, null=True)
    status = models.CharField(max_length=50, null=True, choices=STATUS)

    def __str__(self):
        return self.user


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=1)
    purchased = models.BooleanField(default=False)
    product = models.ForeignKey(Products, null=True, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.name


class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    feedback = models.CharField(max_length=500)
    date = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
