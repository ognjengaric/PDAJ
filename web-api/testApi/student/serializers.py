from .models import Student, Grade
from rest_framework import serializers


class GradeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Grade
        fields = ['id', 'course', 'value']


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    # grades = GradeSerializer(many=True)
    class Meta:
        model = Student
        fields = ['id', 'name', 'last_name', 'index', 'year']
