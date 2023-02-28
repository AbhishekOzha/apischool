from rest_framework import serializers
from .models import School

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('id', 'school_name', 'school_address', 'teachers_list', 'total_students')

class SchoolAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('id', 'school_name', 'school_address', 'teachers_list', 'total_students')

class SchoolTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('id', 'school_name', 'school_address', 'teachers_list')

class SchoolStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('id', 'school_name', 'school_address', 'total_students')
