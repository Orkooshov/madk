from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey


class Subject(models.Model):
    name = models.CharField(max_length=50, unique=True)
    code = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'


class Classroom(models.Model):
    number = models.IntegerField()
    floor = models.IntegerField()
    building = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.building}.{self.floor}.{self.number}"

    class Meta:
        ordering = ['building', 'floor', 'number']
        verbose_name = 'Кабинет'
        verbose_name_plural = 'Кабинеты'


class Teacher(models.Model):
    surname = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)
    classroom = models.ForeignKey(
        Classroom, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self) -> str:
        # classroom_str = f"({self.classroom})" if self.classroom is not None else ''
        return f"{self.surname} {self.name} {self.patronymic}"

    class Meta:
        ordering = ['surname', 'name', 'patronymic']
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'


class Teacher_Subject(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.teacher} - {self.subject}"


class Group(models.Model):
    name = models.CharField(max_length=30, unique=True)
    curator = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class Weekday(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['pk']
        verbose_name = 'День недели'
        verbose_name_plural = 'Дни недели'


class ScheduleStatus(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['pk']
        verbose_name = 'Этап обучения'
        verbose_name_plural = 'Этапы обучения'


class Week(models.Model):
    number = models.IntegerField()

    def __str__(self) -> str:
        return str(self.number)

    class Meta:
        ordering = ['number']
        verbose_name = 'Неделя'
        verbose_name_plural = 'Недели'


class Subgroup(models.Model):
    number = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.number}"

    class Meta:
        ordering = ['number']
        verbose_name = 'Подгруппа'
        verbose_name_plural = 'Подгруппы'


class Schedule(models.Model):
    weekday = models.ForeignKey(Weekday, on_delete=models.CASCADE)
    week = models.ForeignKey(
        Week, on_delete=models.CASCADE, blank=True, null=True)
    position = models.IntegerField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    classroom = models.ForeignKey(
        Classroom, blank=True, null=True, on_delete=models.CASCADE)
    status = models.ForeignKey(
        ScheduleStatus, on_delete=models.CASCADE)
    subgroup = models.ForeignKey(
        Subgroup, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self) -> str:
        return f"schedule"

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписания'
