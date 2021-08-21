from django.db import models
from django.urls import reverse
import datetime as dt


class Subject(models.Model):
    name = models.CharField(max_length=50, unique=True,
                            verbose_name='Название')
    code = models.CharField(max_length=10, blank=True,
                            null=True, verbose_name='Код')

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'


class Classroom(models.Model):
    building = models.IntegerField(verbose_name='Строение')
    floor = models.IntegerField(verbose_name='Этаж')
    number = models.IntegerField(verbose_name='Кабинет')

    def __str__(self) -> str:
        return f"{self.building}.{self.floor}.{self.number}"

    class Meta:
        ordering = ['building', 'floor', 'number']
        verbose_name = 'Кабинет'
        verbose_name_plural = 'Кабинеты'


class Teacher(models.Model):
    surname = models.CharField(max_length=50, verbose_name='Фамилия')
    name = models.CharField(max_length=50, verbose_name='Имя')
    patronymic = models.CharField(max_length=50, verbose_name='Отчество')
    classroom = models.ForeignKey(
        Classroom, on_delete=models.CASCADE,
        blank=True, null=True, verbose_name='Кабинет'
    )
    slug = models.SlugField(max_length=50, unique=True,
                            db_index=True, verbose_name='URL')

    def __str__(self) -> str:
        return f"{self.surname} {self.name} {self.patronymic}"

    class Meta:
        ordering = ['surname', 'name', 'patronymic']
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'


class Group(models.Model):
    name = models.CharField(max_length=30, unique=True,
                            verbose_name='Название')
    curator = models.ForeignKey(
        Teacher, on_delete=models.CASCADE,
        blank=True, null=True, verbose_name='Куратор')
    slug = models.SlugField(max_length=50, unique=True,
                            db_index=True, verbose_name='URL')

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('group_detail', kwargs={'group_slug': self.slug})

    class Meta:
        ordering = ['name']
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class Schedule(models.Model):

    class Weekday(models.IntegerChoices):
        MONDAY = 1, 'Понедельник'
        TUESDAY = 2, 'Вторник'
        WEDNESDAY = 3, 'Среда'
        THURSDAY = 4, 'Четверг'
        FRIDAY = 5, 'Пятница'
        SATURDAY = 6, 'Суббота'
        SUNDAY = 7, 'Воскресенье'
    weekday = models.IntegerField(
        choices=Weekday.choices, verbose_name='День недели')

    class Week(models.IntegerChoices):
        ALL = 0, 'Обе недели'  # default
        FIRST = 1, 'Первая неделя'
        SECOND = 2, 'Вторая неделя'
    week = models.IntegerField(
        choices=Week.choices, default=Week.ALL, verbose_name='Неделя')

    class Position(models.IntegerChoices):
        FIRST = 1, 'Первая пара'
        SECOND = 2, 'Вторая пара'
        THIRD = 3, 'Третья пара'
        FOURTH = 4, 'Четвертая пара'
        FIFTH = 5, 'Пятая пара'
    position = models.IntegerField(
        choices=Position.choices, verbose_name='Пара')
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, verbose_name='Группа')
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, verbose_name='Предмет')
    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, verbose_name='Преподаватель')
    classroom = models.ForeignKey(
        Classroom, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Кабинет')

    class Status(models.IntegerChoices):
        INACTIVE = 0, 'Не активен'
        STUDY = 1, 'Учеба'  # default
        PRACTICE = 2, 'Практика'
        EXAMS = 3, 'Экзамены'
    status = models.IntegerField(
        choices=Status.choices, default=Status.STUDY, verbose_name='Состояние')

    class Subgroup(models.IntegerChoices):
        ALL = 0, 'Вся группа'  # default
        FIRST = 1, 'Первая подгруппа'
        SECOND = 2, 'Вторая подгруппа'
    subgroup = models.IntegerField(
        choices=Subgroup.choices,
        default=Subgroup.ALL,
        verbose_name='Подгруппа'
    )

    def get_timing(self) -> str:
        timings = (
            '9:00 - 10:30',
            '10:40 - 12:10',
            '12:50 - 14:20',
            '14:30 - 16:00',
            '16:10 - 17:40',
        )
        return timings[self.position-1]

    class Meta:
        ordering = ['group', 'weekday', 'position', 'week', 'subgroup']
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписания'
