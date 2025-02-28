from django.db import models

CHOICES_PREDPRIYATIYA = [
    ('LTZ', 'ЛТЗ'),
    ('Mashzavod', 'Машзавод'),
    ('Agregatny_zavod', 'Агрегатный завод'),
    ('HleboKombinat', 'Хлебокомбинат'),
    ('Ludinovokabel', 'Людиновокабель'),
    ('Shveynaya_fabrika', 'Швейная фабрика'),
    ('OEZ', 'ОЭЗ'),
    ("SCHZ", 'СЧЗ'),
    ("other", 'Другое'),
]
class Person(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="Полное ФИО")
    nazvanie = models.CharField(
        max_length=50,
        choices=CHOICES_PREDPRIYATIYA,
        verbose_name="название предприятия",
        unique=True  # Добавил unique, чтобы названия не повторялись. Уберите, если нужно.
    )
    biography = models.TextField(blank=True, verbose_name="Биография/Информация") # позволяет пустые значения
    image1 = models.ImageField(blank=True, upload_to='static/assets/images', verbose_name="Изображение (главное)")
    image2 = models.ImageField(blank=True, upload_to='static/assets/images', verbose_name="Дополнительное изображение(1)")
    image3 = models.ImageField(blank=True, upload_to='static/assets/images', verbose_name="Дополнительное изображение(2)")
    image4 = models.ImageField(blank=True, upload_to='static/assets/images', verbose_name="Дополнительное изображение(3)")
    image5 = models.ImageField(blank=True, upload_to='static/assets/images', verbose_name="Дополнительное изображение(4)")


    class Meta:
        verbose_name = "работник предприятий"
        verbose_name_plural = "работники предприятий"


    def __str__(self):
        return self.full_name
