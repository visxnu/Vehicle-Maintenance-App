from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name

class InsuranceClaim(models.Model):
    claim_type = models.CharField(max_length=100)
    details = models.TextField()

    def __str__(self):
        return self.claim_type
