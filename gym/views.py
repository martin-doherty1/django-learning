from rest_framework import viewsets
from gym.models import Exercise, Sets
from gym.serializers import ExerciseSerializer, SetsSerializer


class ExerciseViewSet(viewsets.ModelViewSet):
    serializer_class = ExerciseSerializer
    queryset = Exercise.objects.all()


class SetsViewSet(viewsets.ModelViewSet):
    serializer_class = SetsSerializer
    queryset = Sets.objects.all()
