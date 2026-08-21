from django.db import models
# from accounts.models import User
from django.conf import settings

class Category(models.Model):

    INCOME = "income" 
    EXPENSE = "expense"

    name = models.CharField(max_length=200)
    type = models.CharField(max_length=10, choices=[(INCOME, "Entré"), (EXPENSE, "Sortie")])

    def __str__(self):
        return self.name


class Transaction(models.Model):

    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="transactions",)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="transactions", )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.CharField(max_length=1000, blank=True)


    def __str__(self):
        return f"{self.category} - {self.amount}"

    #Create your models here.
