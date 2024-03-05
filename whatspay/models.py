from django.db import models


class Item(models.Model):
    class Meta:
        verbose_name = 'Элкмент'
        verbose_name_plural = 'Элементы'

    name = models.CharField(max_length=64, )
    description = models.TextField(blank=True, null=True)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    
    def get_price(self):
        return f'{self.price / 100:.2f}'


