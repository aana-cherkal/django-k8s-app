from django.db import models

# Create your models here.
class Item(models.Model):
    
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=500)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500, default='https://www.jagota.com/wp-content/uploads/2023/04/bgr_item2-image-1024x709.jpg')
    
    def __str__(self):
        return self.item_name
    