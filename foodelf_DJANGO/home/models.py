import datetime
from django.db import models
from django.utils import timezone
from manageTables.models import Customer, ActiveTables

class Item(models.Model):
    item_id = models.IntegerField(default=0)
    item_name = models.CharField(max_length=200)
    price = models.FloatField(default=0)
    ingredients = models.CharField(max_length=200)
    def __str__(self):
        return self.item_name
class Choice(models.Model):
    item = models.ForeignKey(Item,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    table = models.ForeignKey(ActiveTables,on_delete=models.CASCADE,null=True)  #so choices can be associated to tables without having to be claimed by customers yet
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)   # so choices can be associated to specific customers
    date = models.DateTimeField('date of purchase')
    def _str__(self):
        return self.item
    def was_purchased_recently(self):
        return self.date >= timezone.now() - datetime.timedelta(days=1)
# Create your models here.
