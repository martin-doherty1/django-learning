from django.test import TestCase

from gym.models import Exercise


# Create your tests here.
def create_exercise(exercise_name, body_part, description, ty="BB"):
    return Exercise.objects.create(exercise_name=exercise_name, body_part=body_part, description=description, type=ty)
