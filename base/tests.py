from django.test import TestCase
from base.models import Exercise, ExSet, Workout

class ExSetTest(TestCase):
    def test_exset_feature(self):
        # Create your tests here.
        workout = Workout.objects.create(intensity="Medium", name="Chest")
        
        bench_press = Exercise.objects.create(name='Bench Press', 
            category="Weighted")

        bench_press_set = ExSet.objects.create(exercise=bench_press, weight=50, reps=12, 
            workout=workout)
        bench_press_set = ExSet.objects.create(exercise=bench_press, weight=50, reps=12, 
            workout=workout)

        for i in ExSet.objects.filter(workout=workout):
            print(f'{i.exercise.name} | {i.weight} | {i.reps}')

