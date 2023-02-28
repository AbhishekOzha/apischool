from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import School
from .serializers import SchoolSerializer, SchoolAdminSerializer, SchoolTeacherSerializer, SchoolStudentSerializer

class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()

    def get_serializer_class(self):
        user_role = self.request.user.role

        if user_role == 'admin':
            return SchoolAdminSerializer
        elif user_role == 'teacher':
            return SchoolTeacherSerializer
        elif user_role == 'student':
            return SchoolStudentSerializer
        else:
            return SchoolSerializer

    def get_permissions(self):
        user_role = self.request.user.role

        if user_role == 'admin':
            permission_classes = [IsAuthenticated]
        elif user_role == 'teacher':
            permission_classes = [IsAuthenticated]
        elif user_role == 'student':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = []

        return [permission() for permission in permission_classes]
