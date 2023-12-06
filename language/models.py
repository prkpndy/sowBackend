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