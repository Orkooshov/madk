from django.db import models


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
    name = models.CharField(max_length=16)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['pk']
        verbose_name = 'День недели'
        verbose_name_plural = 'Дни недели'


class Schedule(models.Model):

    class Weekday(models.IntegerChoices):
        MONDAY = 1, 'Понедельник'
        TUESDAY = 2, 'Вторник'
        WEDNESDAY = 3, 'Среда'
        THURSDAY = 4, 'Четверг'
        FRIDAY = 5, 'Пятница'
        SATURDAY = 6, 'Суббота'
        SUNDAY = 7, 'Воскресенье'
    weekday = models.IntegerField(choices=Weekday.choices)

    class Week(models.IntegerChoices):
        ALL = 0, 'Все недели' # default
        FIRST = 1, 'Первая неделя'
        SECOND = 2, 'Вторая неделя'
    week = models.IntegerField(choices=Week.choices, default=Week.ALL)

    position = models.IntegerField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    classroom = models.ForeignKey(
        Classroom, blank=True, null=True, on_delete=models.CASCADE)

    class Status(models.IntegerChoices):
        PRACTICE = 0, 'Практика'
        STUDY = 1, 'Учеба'  # default
        EXAMS = 2, 'Экзамены'
    status = models.IntegerField(choices=Status.choices, default=Status.STUDY)

    class Subgroup(models.IntegerChoices):
        ALL = 0, 'Вся группа'  # default
        FIRST = 1, 'Первая подгруппа'
        SECOND = 2, 'Вторая подгруппа'
    subgroup = models.IntegerField(
        choices=Subgroup.choices,
        default=Subgroup.ALL,
        verbose_name='Подгруппа'
    )

    def __str__(self) -> str:
        return f"schedule"

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписания'
