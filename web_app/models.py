from django.db import models


class QuoteRequest(models.Model):

    SERVICE_CHOICES = (
        ('Black', 'Black Box'),
        ('Gray', 'Gray Box'),
        ('White', 'White Box'),
    )

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)
    email = models.EmailField(max_length=254, blank=True)
    company = models.CharField(max_length=100, blank=True)
    service = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    message = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email} - {self.company} - {self.message}"


