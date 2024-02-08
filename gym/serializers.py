from rest_framework import serializers

from gym.models import Exercise, Sets


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'


class SetsSerializer(serializers.ModelSerializer):
    setExercise = ExerciseSerializer(many=True)

    class Meta:
        model = Sets
        fields = '__all__'


class AggregationSerializer(serializers.Serializer):
    key = serializers.CharField()
    doc_count = serializers.IntegerField()

