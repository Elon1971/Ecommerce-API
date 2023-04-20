from django.db import models

class API(models.Model):
    id = models.IntegerField(primary_key=True, null=False)
    discounted_price = models.CharField(max_length=255, null=True)
    Product_image = models.CharField(max_length=255, null=True)
    Description = models.CharField(max_length=2550, null=True)
    Original_price = models.CharField(max_length=255, null=True)
    item_number = models.CharField(max_length=255, null=True)
    attribute_dic = models.TextField(max_length=255, null=True)

    class Meta:
        db_table = 'urls'
