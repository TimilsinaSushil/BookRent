from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        # return str(self.name)
        return f"Author : {self.name}"