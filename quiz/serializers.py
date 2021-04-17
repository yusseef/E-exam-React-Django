from rest_framework import serializers
from .models import Quizzes, Question


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quizzes
        fields = [
            'title',
        ]

class RandomQuestionsSerializer(serializers.ModelSerializer):
    class Meta():
        model = Question
        fields = [
            'title',
            'answer'
        ]