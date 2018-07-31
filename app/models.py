from django.db import models

class User(models.Model):
    name = models.CharField(max_length=20)
    user_id = models.CharField(max_length=15)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.user_id
