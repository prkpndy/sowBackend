from django.db import models

# Table to store term data
class Terms(models.Model):
  key = models.CharField(max_length=30)
  value = models.TextField()

  def __str__(self) -> str:
    return self.key

# Table to store us data
class Us(models.Model):
  key = models.CharField(max_length=30)
  value = models.TextField()

  def __str__(self) -> str:
    return self.key

# Table to store navigation data
class Navigation(models.Model):
  key = models.CharField(max_length=30)
  name = models.CharField(max_length=50)
  link = models.TextField()

  def __str__(self) ->str:
    return self.key

# Table to store price list page information
class PriceListInfo(models.Model):
  key = models.CharField(max_length=30)
  value = models.TextField()

  def __str__(self) -> str:
    return self.key