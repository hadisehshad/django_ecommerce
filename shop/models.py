from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product')
    name = models.CharField(max_length=255)
    description = models.TextField()
    stock = models.IntegerField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    specification = models.TextField()

    def __str__(self):
        return f"{self.id} -{self.name} - {self.category}"