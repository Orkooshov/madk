from django import forms
from django.db.models import fields
from schedule.models import Teacher

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['surname', 'name', 'patronymic']
