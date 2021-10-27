from django.db import models
from django.contrib.auth import get_user_model
# from django.contrib.gis.db import models


User = get_user_model()


# class Category(models.Model):
#     title = models.CharField("Название", max_length=120, null=True)
#
#     def __str__(self):
#         return str(self.title)
#
#     class Meta:
#         verbose_name = "Категория"
#         verbose_name_plural = "Категории"


class Product(models.Model):
    OUTWEAR = 'outwear'
    PANTS = 'pants'
    SHOES = 'shoes'
    ACC = 'accessories'

    CHOICE_GROUP = {
        (OUTWEAR, 'outwear'),
        (PANTS, 'pants'),
        (SHOES, 'shoes'),
        (ACC, 'accessories'),
    }
    title = models.CharField("Название", max_length=100)
    sub_title = models.CharField("Краткое описание", max_length=100, null=True)
    description = models.TextField("Описание")
    composition = models.CharField("Состав", max_length=100, null= True)
    size = models.CharField("Размер", max_length=50, null=True)
    model = models.CharField("Модель и Образ", max_length=150, null=True)
    image = models.ImageField("Изображение",  upload_to="images/", null=True)
    price = models.DecimalField("Цена", default=0, max_digits=10, decimal_places=2)
    group = models.CharField(max_length=20, choices=CHOICE_GROUP, default=OUTWEAR)
    is_active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Comments(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name="Пользователь",
        on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(
         Product,
         verbose_name="Новость",
         on_delete=models.CASCADE, null=True)
    text = models.TextField("Комментарий", null=True)
    created = models.DateTimeField("Дата добавления", auto_now_add=True, null=True)
    moderation = models.BooleanField("Модерация", default=False, null=True)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return "{}".format(self.user)


class Employee(models.Model):
    name = models.CharField("Фио сотрудника", max_length=100)
    position = models.CharField("Должность", max_length=100)
    image = models.ImageField("Изображение",  upload_to="images/", null=True)
    description = models.CharField("Описание", max_length=150)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"


class Message(models.Model):
    full_name = models.CharField("ФИО", max_length=150)
    email = models.EmailField("email", max_length=100)
    title = models.CharField("Заголовок", max_length=100)
    text = models.TextField("Текст", max_length=200)

    def __str__(self):
        return str(self.full_name)

    class Meta:
        verbose_name = "Сообщения"
        verbose_name_plural = "Сообщении"


class Order(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name="Пользователь",
        on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    count = models.IntegerField("Количество")
    size = models.CharField("Размер", max_length=50)
    moderation = models.BooleanField("Модерация", default=False, null=True)

    def __str__(self):
        return "{}".format(self.user)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class Contact(models.Model):
    long_position = models.FloatField()
    lat_position = models.FloatField()
    country = models.CharField("Страна", max_length=30, null=True)
    city = models.CharField("Город", max_length=30, null=True)
    street = models.CharField("Улица", max_length=30, null=True)
    phone_number = models.CharField("Номер телефона", max_length=30, null=True)
    facebook = models.URLField("URl для facebook странице", null=True)
    twitter = models.URLField("URl для twitter странице", null=True)
    linkedin = models.URLField("URl для linkedin странице", null=True)
    behance = models.URLField("URl для behance странице", null=True)

    def __str__(self):
        return str(self.country)

    class Meta:
        verbose_name = "Адрес"
        verbose_name_plural = "Адреса"
# Create your models here.


# class Address(models.Model):
#     country = models.CharField("Страна", max_length=30)
#     city = models.CharField("Город", max_length=30)
#     street = models.CharField("Улица", max_length=30)
#     phone_number = models.CharField("Номер телефона", max_length=30)
#     facebook = models.URLField("URl для facebook странице")
#     twitter = models.URLField("URl для twitter странице")
#     linkedin = models.URLField("URl для linkedin странице")
#     behance = models.URLField("URl для behance странице")
#
#     def __str__(self):
#         return str(self.country)
#
#     class Meta:
#         verbose_name = "Адрес"
