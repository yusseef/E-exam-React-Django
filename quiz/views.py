from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from .models import  Quizzes,Question
from .serializers import QuizSerializer, RandomQuestionsSerializer, QuestionsSerializer
from rest_framework.views import APIView

class Quiz(generics.ListAPIView):
    serializer_class = QuizSerializer
    queryset = Quizzes.objects.all()

class RandomQuestions(APIView):
    
    def get(self, request, format=None, **kwargs):
        question = Question.objects.filter(quiz__title = kwargs['Topic']).order_by('?')[:1]
        serializer = RandomQuestionsSerializer(question, many= True)
        return Response(serializer.data)

class QuizQuestion(APIView):
    
    def get(self, request, format=None, **kwargs):
        question = Question.objects.filter(quiz__title = kwargs['Topic']).order_by('?')
        serializer = QuestionsSerializer(question, many= True)
        return Response(serializer.data)