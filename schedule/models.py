from django.db import models
from django.db.models.query import QuerySet
from django.urls import reverse
import datetime as dt


class Weekday(models.IntegerChoices):
    MONDAY = 0, 'Понедельник'
    TUESDAY = 1, 'Вторник'
    WEDNESDAY = 2, 'Среда'
    THURSDAY = 3, 'Четверг'
    FRIDAY = 4, 'Пятница'
    SATURDAY = 5, 'Суббота'
    SUNDAY = 6, 'Воскресенье'


class Week(models.IntegerChoices):
    ALL = 0, 'Обе недели'  # default
    FIRST = 1, 'Первая неделя'
    SECOND = 2, 'Вторая неделя'


class Subgroup(models.IntegerChoices):
    ALL = 0, 'Вся группа'  # default
    FIRST = 1, 'Первая подгруппа'
    SECOND = 2, 'Вторая подгруппа'


class Lesson(models.IntegerChoices):
    FIRST = 1, 'Первая пара'
    SECOND = 2, 'Вторая пара'
    THIRD = 3, 'Третья пара'
    FOURTH = 4, 'Четвертая пара'
    FIFTH = 5, 'Пятая пара'


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
    # building = models.IntegerField(verbose_name='Строение')
    # floor = models.IntegerField(verbose_name='Этаж')
    # number = models.IntegerField(verbose_name='Кабинет')
    cabinet = models.CharField(
        verbose_name='Кабинет', max_length=10, null=True)

    def __str__(self) -> str:
        return f"{self.cabinet}"

    class Meta:
        ordering = ['cabinet']
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

    def get_absolute_url(self):
        return reverse('teacher_detail', kwargs={'teacher_slug': self.slug})

    def get_short_name(self):
        l = [self.surname, self.name[0]+'.', self.patronymic[0]+'.']
        return ' '.join(l)

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

    def get_schedule(self, weekday=None):
        def to_list(schedules: QuerySet):
            result = []
            it = iter(schedules)
            for schedule in it:
                if schedule.subgroup != Subgroup.ALL:
                    t = [None, None]
                    if schedule.subgroup == Subgroup.FIRST:
                        t[0] = schedule
                        try:
                            sch = next(it)
                            if sch.subgroup == Subgroup.SECOND:
                                t[1] = sch
                            else:
                                result.append(sch)
                        except:
                            pass
                    else:
                        t[1] = schedule
                    result.append(t)
                else:
                    result.append(schedule)
            return result
        queryset = self.schedule_set.filter(is_active=True)
        if weekday != None:
            queryset = queryset.filter(weekday=weekday)
        return to_list(queryset)

    def get_schedule_today(self):
        weekday = Weekday(dt.date.today().weekday())
        weekday = Weekday(4)  # fix
        return self.get_schedule(weekday)

    def get_schedule_tomorrow(self):
        weekday = Weekday((dt.date.today()+dt.timedelta(days=1)).weekday())
        return self.get_schedule(weekday)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('group_detail', kwargs={'group_slug': self.slug})

    class Meta:
        ordering = ['name']
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


timings = (
    '9:00 - 10:30',
    '10:40 - 12:10',
    '12:50 - 14:20',
    '14:30 - 16:00',
    '16:10 - 17:40',
)


class Schedule(models.Model):
    weekday = models.IntegerField(
        choices=Weekday.choices, verbose_name='День недели')
    week = models.IntegerField(
        choices=Week.choices, default=Week.ALL, verbose_name='Неделя')
    lesson = models.IntegerField(
        choices=Lesson.choices, verbose_name='Пара')
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, verbose_name='Группа')
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, verbose_name='Предмет')
    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE,
        verbose_name='Преподаватель')
    classroom = models.ForeignKey(
        Classroom, blank=True, null=True, on_delete=models.CASCADE,
        verbose_name='Кабинет')
    is_active = models.BooleanField(default=True, verbose_name='Активен?')
    subgroup = models.IntegerField(
        choices=Subgroup.choices,
        default=Subgroup.ALL,
        verbose_name='Подгруппа'
    )

    def get_timing(self) -> str:
        return timings[self.lesson-1]

    def __str__(self) -> str:
        return f'{self.group}:{self.get_weekday_display()}'

    class Meta:
        ordering = ['group', 'weekday', 'lesson', 'week', 'subgroup']
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписания'
