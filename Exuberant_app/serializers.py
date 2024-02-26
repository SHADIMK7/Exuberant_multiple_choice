from rest_framework import serializers
from .models import *


class RegistrationSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = User
        fields = ['username','email','password']

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['question', 'option1', 'option2', 'option3', 'option4', 'correct_option']

    def create(self, validated_data):
        return Question.objects.create(**validated_data)
    
class UserAnswersSerializer(serializers.ModelSerializer):
    question = serializers.SerializerMethodField()

    class Meta:
        model = UserAnswers
        fields = ['user', 'question', 'selected_option']

    def get_question(self, obj):
        return {
            'question': obj.question.question,
            'option1': obj.question.option1,
            'option2': obj.question.option2,
            'option3': obj.question.option3,
            'option4': obj.question.option4,
            'correct_option': obj.question.correct_option
        }