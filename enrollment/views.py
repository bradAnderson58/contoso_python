from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from enrollment.models import Enrollment
from enrollment.serializers import EnrollmentSerializer


class EnrollmentListCreateView(ListCreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer


class EnrollmentView(RetrieveUpdateDestroyAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
