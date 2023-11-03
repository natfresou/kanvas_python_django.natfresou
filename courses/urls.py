from django.urls import path
from . import views


urlpatterns = [
    path("courses/", views.ListCreateCourseView.as_view()),
    path("courses/<str:course_id>/", views.RetrieveUpdateDestroyCourseView.as_view()),
    path("courses/<str:course_id>/contents/", views.CreateContentsView.as_view()),
    path("courses/<str:course_id>/contents/<str:content_id>/", views.RetrieveUpdateDestroyContentView.as_view()),
    path("courses/<str:course_id>/students/", views.RetrieveUpdateStudentsView.as_view()),
]

