from django.db import models


class Record(models.Model):
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
