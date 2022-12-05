from django.db import models
import datetime


class FireExtingusher(models.Model):
    type = models.CharField(max_length=20, verbose_name='Тип')
    weight = models.PositiveIntegerField(verbose_name='Вес')
    repair_coast = models.PositiveIntegerField(verbose_name='Стоимость перезаряда')

    class Meta:
        verbose_name = 'Огнетушитель'
        verbose_name_plural = 'Огнетушители'

    def __str__(self):
        return self.type


class Order(models.Model):
    fire_extingushers = models.ManyToManyField(FireExtingusher, through='OrderPosition', verbose_name='Огнетушители')
    repair = models.BooleanField(default=False, verbose_name='Замена ЗПУ')
    repair_quantity = models.PositiveIntegerField(default=0, verbose_name='Количество замен')
    owner = models.ForeignKey('Office', on_delete=models.CASCADE, related_name='orders', verbose_name='Владелец')
    date_input = models.DateField(auto_now_add=True, verbose_name='Дата приемки')
    date_output = models.DateField(auto_now=True, verbose_name='Дата выдачи')
    status = models.CharField(max_length=20, verbose_name='Состояние')
    description = models.CharField(max_length=200, verbose_name='Описание')

    class Meta:
        verbose_name = 'Партия'
        verbose_name_plural = 'Партии'

    def set_status(self, status):
        if status == 'input':
            self.status = 'принято'
        if status == 'finish':
            self.status = 'готово'
        if status == 'output':
            self.status = 'отдано'

    def time_in_work(self):
        result = datetime.date.today() - self.date_input
        return result.days

    def finish_time(self):
        result = datetime.date.today() - self.date_output
        return result.days

    def __str__(self):
        return f'Партия {self.owner} от {self.date_input}'


class OrderPosition(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='positions', verbose_name='партия')
    fire_ex = models.ForeignKey(FireExtingusher, on_delete=models.CASCADE, related_name='positions', verbose_name='огнетушитель')
    quantity = models.PositiveIntegerField(default=1, verbose_name='количество')

    class Meta:
        verbose_name = 'Позиция'
        verbose_name_plural = 'Позиции'


class Firm(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название')

    class Meta:
        verbose_name = 'Фирма'
        verbose_name_plural = 'Фирмы'

    def __str__(self):
        return self.name


class Office(models.Model):
    firm = models.ForeignKey(Firm, related_name='offices', on_delete=models.CASCADE, verbose_name='Организация')
    adress = models.CharField(max_length=200, verbose_name='Адрес')
    contact = models.CharField(max_length=30, verbose_name='контакт')

    class Meta:
        verbose_name = 'Отделение'
        verbose_name_plural = 'Отделения'

    def __str__(self):
        return f'{self.firm} в {self.adress}'
