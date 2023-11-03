import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    email = models.EmailField(unique=True, max_length = 100)
    is_superuser = models.BooleanField(default=False, null=True)
    my_courses = models.ManyToManyField("courses.Course", through="students_courses.StudentCourse", related_name="students")
