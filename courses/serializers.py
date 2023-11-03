from rest_framework import serializers
from .models import Course
from contents.serializers import ContentSerializer
from students_courses.serializers import StudentCourseSerializer
from rest_framework.validators import UniqueValidator
from accounts.models import Account


class CourseSerializer(serializers.ModelSerializer):
    status = serializers.CharField(read_only=True)
    class Meta:
        model = Course
        fields = [
            "id",
            "name",
            "status",
            "start_date",
            "end_date",
            "instructor",
            "contents",
            "students_courses"
        ]
        extra_kwargs = {"instructor": {"required":False}, "contents": {"read_only":True}, "students_courses": {"read_only":True},"name": {
                "validators": [
                    UniqueValidator(
                        queryset=Course.objects.all(),
                        message="course with this name already exists.",
                    )
                ]
            }}
        

class Course3Serializer(serializers.ModelSerializer):
    status = serializers.CharField(read_only=True)
    contents =  ContentSerializer( read_only=True, many = True)
    students_courses = StudentCourseSerializer( read_only=True, many = True) 
    class Meta:
        model = Course
        fields = [
            "id",
            "name",
            "status",
            "start_date",
            "end_date",
            "instructor",
            "contents",
            "students_courses"
        ]
        extra_kwargs = {"instructor": {"required":False}, "name": {
                "validators": [
                    UniqueValidator(
                        queryset=Course.objects.all(),
                        message="course with this name already exists.",
                    )
                ]
            }}

class Course2Serializer(serializers.ModelSerializer):
    students_courses =StudentCourseSerializer( many = True)
    class Meta:
        model = Course
        fields = [
            "id",
            "name",
            "students_courses"
        ]
        extra_kwargs = { "name": {"read_only": True}}

    def update(self, instance, validated_data):
        list_students=[]
        list_emails = []

        for student in validated_data["students_courses"]:
            estudante= student["student"]
            estudante_encontrado = Account.objects.filter(email=estudante["email"]).first()
            if estudante_encontrado:
                list_students.append(estudante_encontrado)
            else:
                list_emails.append(estudante["email"])
        if list_emails:
            raise serializers.ValidationError({"detail": f"No active accounts was found: {', '.join(list_emails)}." # o join serve pra juntar os emails
})
        if not self.partial:
            instance.students.add(*list_students)
            return instance
        return super().update(instance, validated_data)
        
