from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from course.models import Course
from course.serializers import CourseSerializer


class CourseListCreateView(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseView(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
