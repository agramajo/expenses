from django.db import models
from django.utils import timezone

class Expense(models.Model):
    SOURCE_CHOICES = (
        ('alejandro-banco','Alejandro Banco'),
        ('alejandro-efectivo','Alejandro Efectivo'),
        ('vilma-banco','Vilma Banco'),
    )

    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    value = models.DecimalField(max_digits=6, decimal_places=2,null=True)
    source = models.CharField(max_length=20,choices=SOURCE_CHOICES)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

