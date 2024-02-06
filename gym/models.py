from django.db import models


# Create your models here.

class Exercise(models.Model):
    exercise_name = models.TextField(max_length=50, null=False, blank=False)
    body_part = models.TextField(max_length=5)

    def __str__(self):
        return f'{self.exercise_name} -- {self.body_part}'

    class Meta:
        db_table = 'exercises'


class Sets(models.Model):
    setNumber = models.IntegerField()
    setReps = models.IntegerField()
    setExercise = models.ManyToManyField(to=Exercise, related_name='sets')
    created_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Set {self.setNumber} -- Reps {self.setReps} -- Exercise {self.setExercise}'

    class Meta:
        db_table = 'sets'
