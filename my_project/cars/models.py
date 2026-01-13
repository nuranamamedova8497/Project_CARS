from django.db import models
from django.conf import settings


class Car(models.Model):
    RENT = 'rent'
    SALE = 'sale'
    TYPE_CHOICES = ((RENT, 'rent'), (SALE, 'sale'))
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='cars'
    )
    brand = models.CharField(max_length=500)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    speed = models.PositiveIntegerField(help_text="км/ч")
    image = models.ImageField(upload_to='cars_images/', blank=True, null=True)
    year = models.PositiveIntegerField()
    mileage = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)


    def __str__(self):
        return self.brand

    class Meta:
        ordering = ["-created_at"]



class DealRequest(models.Model):
    WAITING = "waiting"
    APPROVED = "approved"
    REJECTED = "rejected"

    STATUS_CHOICES = [
        (WAITING, "Waiting"),
        (APPROVED, "Approved"),
        (REJECTED, "Rejected"),
    ]

    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    seeker = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name="deal_requests")
    comment = models.TextField()
    date_approved = models.DateTimeField(null=True, blank=True)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=WAITING
    )


    def __str__(self):
        return f"Request №{self.id} on {self.car.brand}"



