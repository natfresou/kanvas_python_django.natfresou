import uuid
from django.db import models


class CourseStatus(models.TextChoices):
    PROGRESS = "in progress"
    FINISHED = "finished"
    DEFAULT = "not started"

class Course(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    status = models.CharField(max_length=11, default= CourseStatus.DEFAULT, choices=CourseStatus.choices)
    name = models.CharField(max_length=100,unique=True)
    start_date = models.DateField()
    end_date = models.DateField()
    instructor = models.ForeignKey(
        "accounts.Account",
        on_delete=models.CASCADE,
        related_name="courses", blank=True, null= True
    )
