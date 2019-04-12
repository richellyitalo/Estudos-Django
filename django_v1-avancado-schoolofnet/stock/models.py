from django.db import models

# Buscar por Meta inheritance
# https://docs.djangoproject.com/en/2.2/topics/db/models/


class TimestampableMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True


class Product(TimestampableMixin):
    name = models.CharField(max_length=255)
    stock = models.IntegerField(default=0)
    stock_max = models.IntegerField()
    price_sale = models.DecimalField(decimal_places=2, max_digits=5)
    price_purchase = models.DecimalField(decimal_places=2, max_digits=5)


class StockEntry(TimestampableMixin):
    amount = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
