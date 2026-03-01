from django.db import models
from django.utils import timezone


class Service(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='services/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    review = models.TextField()
    rating = models.IntegerField(default=5)
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)

    def __str__(self):
        return self.name


class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    mobile = models.CharField(max_length=20)
    message = models.TextField()
    submitted_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} — {self.submitted_at.strftime('%d %b %Y %H:%M')}"

    class Meta:
        ordering = ['-submitted_at']
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'


class QuoteRequest(models.Model):
    SERVICE_CHOICES = [
        ('aluminium_windows', 'Aluminium Windows'),
        ('glass_work', 'Glass Work'),
        ('acp_sheet', 'ACP Sheet'),
        ('hpl_sheet', 'HPL Sheet'),
        ('upvc', 'UPVC Windows & Doors'),
        ('interior_design', 'Interior Design'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=200)
    email = models.EmailField()
    mobile = models.CharField(max_length=20)
    service_type = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    description = models.TextField(help_text='Describe your requirement in detail')
    budget = models.CharField(max_length=100, blank=True, null=True)
    submitted_at = models.DateTimeField(default=timezone.now)
    is_resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} — {self.get_service_type_display()} ({self.submitted_at.strftime('%d %b %Y')})"

    class Meta:
        ordering = ['-submitted_at']
        verbose_name = 'Quote Request'
        verbose_name_plural = 'Quote Requests'


