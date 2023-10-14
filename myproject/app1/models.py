from django.db import models
from django.utils import timezone
# Create your models here.
class SaveCoin(models.Model):
    coin = (("О","Орел"),("Р","Решка"))
    coin_var = models.CharField(max_length=1,choices=coin)
    date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"-{self.coin_var}-  "

    class Meta:
        ordering = ["-date"]
    @staticmethod
    def get_n(n):
        print(SaveCoin.objects.all()[:n])
        return SaveCoin.objects.all()[:n]




# Допишите несколько функций CRUD для работы с моделями по желанию. Что по вашему мнению актуально в такой ба

class Сlient(models.Model):
    # Поля модели «Клиент»:
# — имя клиента
# — электронная почта клиента
# — номер телефона клиента
# — адрес клиента
# — дата регистрации клиента
    name = models.CharField(max_length=20)
    mail = models.CharField(max_length=80)
    telNumber = models.CharField(max_length=11)
    adress = models.CharField(max_length=25)
    date = models.DateTimeField(default=timezone.now)
    def __str__(self) -> str:
        return f'Покупатель:{self.name} почта:{self.mail} телефон:{self.telNumber} адрес:{self.adress}'
    
class Product(models.Model):
# Поля модели «Товар»:
# — название товара
# — описание товара
# — цена товара
# — количество товара
# — дата добавления товара
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=180)
    price = models.FloatField()
    quantity = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)
    def __str__(self) -> str:
        return f'Продукт:{self.name} Описание:{self.product} Цена:{self.total_order} Колличестрво:{self.quantity}'
    
class Order(models.Model):
# Поля модели «Заказ»:
# — связь с моделью «Клиент», указывает на клиента, сделавшего заказ
# — связь с моделью «Товар», указывает на товары, входящие в заказ
# — общая сумма заказа
# — дата оформления заказа
    client = models.ForeignKey(Сlient, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    total_order = models.FloatField()
    date = models.DateTimeField(default=timezone.now)
    def __str__(self) -> str:
        return f'Клиент:{self.client} Продукты:{self.product} Сумма заказа:{self.total_order}'