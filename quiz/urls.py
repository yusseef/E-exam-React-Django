from django.urls import path
from .views import Quiz, RandomQuestions, QuizQuestion

app_name = 'quiz'

urlpatterns = [
        path('', Quiz.as_view(), name = 'quiz'),
        path('r/<str:Topic>/', RandomQuestions.as_view(), name = 'random'),
        path('q/<str:Topic>/', QuizQuestion.as_view(), name = 'questions'),
    ]