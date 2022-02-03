from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from person.models import Person
from person.serializers import PersonSerializer


class PersonListCreateView(ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonView(RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
