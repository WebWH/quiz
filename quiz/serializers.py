from rest_framework import serializers
from .models import Quiz

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz  # Quiz Model 중 아래 필드들을 JSON으로 만들어 줌
        fields = ('title', 'body', 'answer')
