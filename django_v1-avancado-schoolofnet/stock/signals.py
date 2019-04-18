from .models import StockEntry
from django.db.models.signals import post_save, pre_save
from django.dispatch.dispatcher import Signal
from .emails import StockGreaterMax
from django_avancado.settings import MAIL_BOSS


signal_customizado_product_stock_changed = Signal()


def increment_stock(sender, instance, created, **kwargs):
    if created is True:
        product = instance.product
        product.stock += instance.amount
        product.save()
        signal_customizado_product_stock_changed.send(sender=None, instance=product)


def send_mail_stock_max_overload(sender, instance, **kwargs):
    if instance.stock > instance.stock_max:
        StockGreaterMax(instance).send(MAIL_BOSS)


def test_update_post_save(sender, instance, created, **kwargs):
    print('Created? ==> ', created)


def test_pre_save(sender, instance, **kwargs):
    print('PRE_SAVE')
    print('instance ==> ', instance)


# Maneira ~1
post_save.connect(increment_stock, sender=StockEntry)
post_save.connect(test_update_post_save, sender=StockEntry)

pre_save.connect(test_pre_save, sender=StockEntry)
signal_customizado_product_stock_changed.connect(send_mail_stock_max_overload, sender=None)

# Maneira ~2
# lógica em 'app.py' no método 'ready'
