from django.db import models


class Item(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Название',
    )
    description = models.TextField(
        verbose_name='Описание',
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена',
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name
