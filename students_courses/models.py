import uuid
from django.db import models

class StudentCourseStatus(models.TextChoices):
    ACCEPTED = "accepted"
    DEFAULT = "pending"

class StudentCourse(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    status = models.CharField(max_length=20, default= StudentCourseStatus.DEFAULT, choices=StudentCourseStatus.choices)
    course = models.ForeignKey("courses.Course", on_delete = models.PROTECT, related_name="students_courses")
    student = models.ForeignKey("accounts.Account", on_delete = models.PROTECT, related_name="students_courses")

