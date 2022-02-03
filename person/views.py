from rest_framework.generics import ListCreateAPIView

from person.models import Person
from person.serializers import PersonSerializer


class PersonListCreateView(ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

