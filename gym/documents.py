from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from gym.models import Exercise, Sets


@registry.register_document
class ExerciseDocument(Document):
    id = fields.IntegerField()

    class Index:
        name = 'exercises'
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0
                    }

    class Django:
        model = Exercise
        fields = ['exercise_name', 'body_part']


@registry.register_document
class SetsDocument(Document):
    id = fields.IntegerField()
    setExercise = fields.ObjectField(properties={
        "exercise_name": fields.TextField(),
        "body_part": fields.TextField()
    })

    class Index:
        name = 'sets'
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0
                    }

    class Django:
        model = Sets
        fields = ['setNumber', 'setReps', 'created_datetime']
