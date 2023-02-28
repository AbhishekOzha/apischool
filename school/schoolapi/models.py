from django.db import models

class School(models.Model):
    school_name = models.CharField(max_length=30)
    school_address = models.CharField(max_length=30)
    teachers_list = models.IntegerField()
    total_students = models.IntegerField()

    def __str__(self):
        return self.school_name


