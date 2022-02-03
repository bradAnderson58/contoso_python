from rest_framework.serializers import ModelSerializer

from enrollment.models import Enrollment


class EnrollmentSerializer(ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'
