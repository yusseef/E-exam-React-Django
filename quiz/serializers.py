from rest_framework import serializers
from .models import Quizzes, Question, Answer


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quizzes
        fields = [
            'title',
        ]

class AnswerSerlializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields=[
            'id',
            'answer_text',
            'is_right'
        ]

class RandomQuestionsSerializer(serializers.ModelSerializer):
    answer = AnswerSerlializer(many = True, read_only=True)
    class Meta():
        model = Question
        fields = [
            'title',
            'answer'
        ]

class QuestionsSerializer(serializers.ModelSerializer):
    answer = AnswerSerlializer(many = True, read_only=True)
    quiz = QuizSerializer(read_only=True)
    class Meta():
        model = Question
        fields = [
            'quiz',
            'title',
            'answer'
        ]