from django.core.management.base import BaseCommand
from gym.models import Exercise, Sets


class Command(BaseCommand):
    help = "Populates the database with some testing data."

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Started database population process..."))

        if Exercise.objects.filter(exercise_name="bench press").exists():
            self.stdout.write(self.style.SUCCESS("Database has already been populated. Cancelling the operation."))
            return
        
        # create Exercises
        exercise1 = Exercise.objects.create(exercise_name="bench press", body_part="chest", description="stronger pec muscles", type="BB")
        exercise1.save()

        exercise2 = Exercise.objects.create(exercise_name="squat", body_part="legs", description="stronger leg muscles", type="CAB")
        exercise2.save()

        exercise3 = Exercise.objects.create(exercise_name="squat3", body_part="legs", description="stronger leg muscles", type="CAB")
        exercise3.save()

        # create Sets
        set1 = Sets.objects.create(setNumber=1, setReps=8)
        set2 = Sets.objects.create(setNumber=1, setReps=6)

        set1.save()
        set1.setExercise.add(exercise1)
        set2.save()
        set2.setExercise.add(exercise2)

        self.stdout.write(self.style.SUCCESS("Successfully populated the database."))