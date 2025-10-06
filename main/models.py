from django.db import models
from django.contrib.auth.models import User

class Products(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) 
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=50)
    is_featured = models.BooleanField(default=False)
    products_views = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def increment_views(self):
        self.products_views += 1
        self.save()