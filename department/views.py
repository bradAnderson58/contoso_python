from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from department.models import Department
from department.serializers import DepartmentSerializer


class DepartmentListCreateView(ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentView(RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)