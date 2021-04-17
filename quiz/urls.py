from django.urls import path
from .views import Quiz, RandomQuestions

app_name = 'quiz'

urlpatterns = [
        path('', Quiz.as_view(), name = 'quiz'),
        path('r/<str:Topic>/', RandomQuestions.as_view(), name = 'random'),
    ]