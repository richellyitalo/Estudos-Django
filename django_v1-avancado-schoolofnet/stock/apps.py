from django.apps import AppConfig


class StockConfig(AppConfig):
    name = 'stock'

    def ready(self):
        # Maneira ~1
        from stock import signals

        # Maneira ~2
        # from stock.signals import increment_stock
        # from django.db.models.signals import post_save
        #
        # stock_entry_model = self.get_model(model_name='StockEntry')
        # post_save.connect(increment_stock, sender=stock_entry_model)
