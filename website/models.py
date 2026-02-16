from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='services/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    review = models.TextField()
    rating = models.IntegerField(default=5)
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)

    def __str__(self):
        return self.name
