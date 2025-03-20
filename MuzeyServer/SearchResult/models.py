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
        unique=True
    )
    biography = models.TextField(blank=True, verbose_name="Биография/Информация")
    image_main = models.ImageField(blank=True, upload_to='static/assets/images', verbose_name="Изображение (главное)")

    class Meta:
        verbose_name = "работник предприятий"
        verbose_name_plural = "работники предприятий"

    def __str__(self):
        return self.full_name


class ImagePerson(models.Model):
    filename = models.ImageField(blank=True, upload_to='static/assets/images', verbose_name="Изображение")
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='images', verbose_name="Работник")
    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"

    def __str__(self):
        return self.filename.name
