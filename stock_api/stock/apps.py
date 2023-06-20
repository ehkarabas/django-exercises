from django.apps import AppConfig


class StockConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'stock'

    # application'i ayaga kaldir, is bitince stock.signals.py dosyasini calistir.
    def ready(self):
        import stock.signals
