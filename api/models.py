from django.db import models # type: ignore

# Create your models here.
class UserModel(models.Model):
    user_id = models.IntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    is_Admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class ProductModel(models.Model):
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=100)
    product_desc = models.CharField(max_length=100)
    product_qty = models.IntegerField()
    product_price = models.IntegerField()
    product_img = models.ImageField(upload_to='images/', default="")

    def __str__(self):
        return self.product_name

    
    