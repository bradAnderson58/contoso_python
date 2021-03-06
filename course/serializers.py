from rest_framework.serializers import ModelSerializer

from course.models import Course
from person.serializers import PersonSerializer


class CourseSerializer(ModelSerializer):
    instructors = PersonSerializer(many=True, required=False, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'
