from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
CATEGORIES = [('other', 'Разное'),
              ('gadgets', 'Гаджеты'),
              ('auto', 'Авто'),
              ('health', 'Здоровье'),
              ('education', 'Образование')]


class Product(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name="Наименование", )
    category = models.CharField(max_length=30, default='other', choices=CATEGORIES, verbose_name="Категория")
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание')
    picture = models.ImageField(verbose_name="Картинка", upload_to="products/", null=True, blank=True)

    def __str__(self):
        return f" {self.title}, {self.category}"

    class Meta:
        db_table = 'products'
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Review(models.Model):
    product = models.ForeignKey(
        'webapp.Product',
        on_delete=models.CASCADE,
        related_name='product',
        verbose_name="Продукт"
    )
    review_text = models.TextField(
        max_length=2000,
        null=False,
        blank=False,
        verbose_name="Текст отзыва"
    )
    grade = models.PositiveIntegerField(
        validators=[MinValueValidator(1),
                    MaxValueValidator(5)],
        null=False,
        blank=False,
        verbose_name="Оценка"
    )
    moderated = models.BooleanField(
        default=False,
        verbose_name="Промодерирован"
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        return f"{self.review_text}, {self.grade}"

    class Meta:
        db_table = 'reviews'
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
