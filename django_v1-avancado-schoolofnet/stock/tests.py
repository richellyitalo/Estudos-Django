from django.contrib.auth.models import User
from django.test import TestCase
from django.test.testcases import SimpleTestCase
from .models import Product, TimestampableMixin, StockEntry
from django.shortcuts import reverse


# SimpleTestCase não utiliza registros no banco
# apenas situações com base nos models, etc
class ProductTest(SimpleTestCase):
    def test_product_initial_stock_field(self):
        product = Product()
        self.assertEquals(0, product.stock)

    def test_product_is_instaceof_timestampablemixin(self):
        product = Product()
        self.assertIsInstance(product, TimestampableMixin)
        # self.assertNotIsInstance(product, TimestampableMixin)

    def test_exception_when_stock_less_then_zero(self):
        product = Product()
        with self.assertRaises(ValueError) as exception:
            product.stock = 10
            product.decrement(11)
        self.assertEquals('Sem estoque disponível', str(exception.exception))


# TestCase para trabalhar com banco de dados
class ProductDatabaseTest(TestCase):
    fixtures = ['auth.json', 'data.yaml']

    def setUp(self):
        self.product = Product.objects.create(
            name='Produto YY', stock_max=200, price_sale=50.00, price_purchase=20.00
        )

    def test_product_save(self):
        self.assertEquals('Produto YY', self.product.name)
        self.assertEquals(0, self.product.stock)

    def test_if_user_exists(self):
        user = User.objects.all().first()
        self.assertIsNotNone(user)


class StockEntryHttpTest(TestCase):
    fixtures = ['data.yaml']

    def test_list(self):
        response = self.client.get('/stock_entries/')
        self.assertEquals(200, response.status_code)
        self.assertIn('Produto BB', str(response.content))

    def test_create(self):
        url = reverse('stock-create')
        stock_params = {'product': 1, 'amount': 20}
        self.client.post(url, stock_params)
        entry_stock = StockEntry.objects.filter(amount=20, product_id=1).first()
        self.assertIsNotNone(entry_stock)
        self.assertEquals(40, entry_stock.product.stock)
