from django.db import models


class World(models.Model):
    name = models.CharField(max_length=100, unique=True)
    hello_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def send_hello(self):
        self.hello_count += 1
        self.save()
