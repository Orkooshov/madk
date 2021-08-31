from rest_framework import serializers
from . import models as m


class SubjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = m.Subject
        fields = 'name', 'code'


class ClassroomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = m.Classroom
        fields = 'building', 'floor', 'number'


class TeacherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = m.Teacher
        fields = '__all__'


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = m.Group
        fields = '__all__'

class ScheduleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = m.Schedule
        fields = '__all__'