from django.db import models

# Table to store pricelist
class PriceListItems(models.Model):
  article_number = models.PositiveIntegerField()
  name = models.CharField(max_length=50)
  in_price = models.PositiveIntegerField()
  price = models.PositiveIntegerField()
  in_stock = models.CharField(max_length=10)
  unit = models.PositiveIntegerField()
  description = models.TextField()

  def __str__(self) -> str:
    return self.name
