from django.db import models
"""
Последовательность из двух кортежей для выбора в этом поле. Если это задано, виджет формы по умолчанию будет 
представлять собой поле выбора вместо стандартного текстового поля и будет ограничивать выбор заданными вариантами. 
"""


class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)


class Runner(models.Model):
    MedalType = models.TextChoices('MedalType', 'GOLD SILVER BRONZE')
    name = models.CharField(max_length=60)
    medal = models.CharField(blank=True, choices=MedalType.choices, max_length=10)


