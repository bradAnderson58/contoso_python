from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from course.models import Course
from course.serializers import CourseSerializer
from person.models import Person


class CourseListCreateView(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def perform_create(self, serializer):
        course = serializer.save()
        if 'instructors' in serializer.initial_data:
            instructor_list = serializer.initial_data.pop('instructors')
            instructors = [Person.objects.get(id=i.get('id')) for i in instructor_list]
            course.instructors.set(instructors)


class CourseView(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def perform_update(self, serializer):
        serializer.save()
        if 'instructors' in serializer.initial_data:
            instructor_list = serializer.initial_data.pop('instructors')
            instructors = [Person.objects.get(id=i.get('id')) for i in instructor_list]
            serializer.instance.instructors.set(instructors)
