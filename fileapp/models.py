from django.db import models

class product_list(models.Model):
    Product_name = models.CharField(max_length=100,null=True)
    Product_price = models.IntegerField(null=True)
    Product_quantity = models.IntegerField(null=True)
    Image = models.ImageField(upload_to="image/", null=True)
