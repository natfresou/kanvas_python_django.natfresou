from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView, CreateAPIView,RetrieveUpdateAPIView
from .models import Course
from django.shortcuts import get_object_or_404
from .serializers import CourseSerializer, Course2Serializer,Course3Serializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsSuperuserOrReadOnly,IsSuperuserOrOwner,IsSuperuser,IsSuperuserOrOwnerForGet,IsSuperuserOrOwnerForGet2
from rest_framework.permissions import IsAuthenticated
from contents.models import Content
from contents.serializers import ContentSerializer
from rest_framework.exceptions import NotFound
from drf_spectacular.utils import extend_schema

@extend_schema(
            tags = ["Criação e listagem de cursos"] 
            )
class ListCreateCourseView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated,IsSuperuserOrReadOnly]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_queryset(self):
        if not self.request.user.is_superuser:
            return Course.objects.filter(students=self.request.user)
        return Course.objects.all()

@extend_schema(
            tags = ["Listagem por id, edição e exclusão de um curso"] 
            )
class RetrieveUpdateDestroyCourseView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsSuperuserOrOwner]
    queryset = Course.objects.all()
    serializer_class = Course3Serializer
    lookup_url_kwarg = "course_id" 

@extend_schema(
            tags = ["Criação de conteúdo de um curso"] 
            )
class CreateContentsView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsSuperuser]
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    lookup_url_kwarg = "course_id" 

    def perform_create(self, serializer):
        course=get_object_or_404(Course,id= self.kwargs["course_id"])
        serializer.save(course=course)

@extend_schema(
            tags = ["Matrícula de estudante em um curso e listagem de estudantes matriculados"] 
            )
class RetrieveUpdateStudentsView( RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated,IsSuperuserOrOwner]
    queryset = Course.objects.all()
    serializer_class = Course2Serializer
    lookup_url_kwarg = "course_id" 


@extend_schema(
            tags = ["Listagem por id, edição e exclusão de conteúdo de curso"] 
            )
class RetrieveUpdateDestroyContentView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsSuperuserOrOwnerForGet]
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    # lookup_url_kwarg = ['course_id','course_id']


    def get_object(self):

        course_get = self.kwargs.get('course_id')
        content_get = self.kwargs.get('content_id')
        
        try:
            course_obj = Course.objects.get(id=course_get) # usar metodos que estourem erro. o Filter não estoura.
    
        except Course.DoesNotExist:
            raise NotFound({'detail': 'course not found.'})
        try:
            content_obj = Content.objects.get(id=content_get)
        except Content.DoesNotExist:
            raise NotFound({'detail': 'content not found.'})
        
        
        obj = Content.objects.get(id=content_get, course=course_obj)

        
        self.check_object_permissions(self.request,  obj )

        return  obj 


    