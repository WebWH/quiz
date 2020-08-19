from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Quiz
from .serializers import QuizSerializer
import random

@api_view(['GET'])
def helloAPI(request):
    return Response('Hello World!')

# 주어진 개수만큼의 퀴즈를 반환
@api_view(['GET'])
def randomQuiz(request, id):
    totalQuizs = Quiz.objects.all()
    randomQuizs = random.sample(list(totalQuizs), id)  # id:개수
    serializer = QuizSerializer(randomQuizs, many=True)  # many=True : 다량의 데이터도 직렬화
    return Response(serializer.data)