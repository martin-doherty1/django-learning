from django.db import models

EXERCISE_TYPE = [
    ("BB", "Barbell"),
    ("CAB", "Cable"),
    ("DB", "Dumbbell"),
    ("BW", "Body Weight")
]


class Exercise(models.Model):
    exercise_name = models.TextField(max_length=50, null=False, blank=False)
    body_part = models.TextField(max_length=5)
    description = models.TextField(max_length=300, null=False, blank=False, default="basic exercise description")
    type = models.CharField(max_length=5, choices=EXERCISE_TYPE, default="BB")

    def __str__(self):
        return f'{self.exercise_name} -- {self.body_part}'

    class Meta:
        db_table = 'exercises'

    def type_to_string(self):
        if self.type == "BB":
            return "Barbell"
        elif self.type == "CAB":
            return "Cable"
        elif self.type == "DB":
            return "Dumbbell"
        elif self.type == "BW":
            return "Body Weight"


class Sets(models.Model):
    setNumber = models.IntegerField()
    setReps = models.IntegerField()
    setExercise = models.ManyToManyField(to=Exercise, related_name='sets')
    created_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Set {self.setNumber} -- Reps {self.setReps} -- Exercise {self.setExercise}'

    class Meta:
        db_table = 'sets'
