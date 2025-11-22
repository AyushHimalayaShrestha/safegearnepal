from django.db import models

# Create your models here.
class Supplier(models.Model):
    name = models.CharField(max_length=255)
    contact_person =models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.TextField()
    created_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name