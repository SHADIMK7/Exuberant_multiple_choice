# views.py
from django.shortcuts import get_object_or_404
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework .response import Response
from rest_framework .views import APIView
from rest_framework import permissions
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated


class Registration(generics.CreateAPIView):
    serializer_class = RegistrationSerializer
        
    def post(self, request):
        
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            account = serializer.save()
            
            # Create or retrieve token for the user
            token, created = Token.objects.get_or_create(user=account)
            token_key = token.key

            data = {
                'response': "REGISTRATION SUCCESSFUL",
                'username': account.username,
                'token': token_key
            }
        else:
            data = serializer.errors
        return Response(data)


    
class Logout(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response({"detail": "Successfully logged out."}, status=status.HTTP_200_OK)

class QuestionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class UserAnswerAPIView(APIView):
    permission_classes= [IsAuthenticated]
    serializer_class = UserAnswersSerializer
    
    def post(self, request, *args, **kwargs):
        question_id = kwargs.get('pk')
        question = get_object_or_404(Question, pk=question_id)
        print(request.user.id,"user")
        
        data = {'user': request.user.id, 'question': question_id, 'selected_option': request.data.get('selected_option')}
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save(question=question)
            return Response({'status': "success", 'message': "Answer submitted successfully", 'response_code': status.HTTP_201_CREATED})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserTotalScoreAPIView(APIView):
    permission_classes= [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        total_questions = Question.objects.count()

        user = request.user

        answered_questions = set(UserAnswers.objects.filter(user=user).values_list('question', flat=True))

        correct_answers_count = 0
        incorrect_answers_count = 0

        for question_id in answered_questions:
            question = Question.objects.get(pk=question_id)
            correct_option = question.correct_option

            latest_answer = UserAnswers.objects.filter(user=user, question=question_id).latest('id')
            if latest_answer.selected_option == correct_option:
                correct_answers_count += 1
            else:
                incorrect_answers_count += 1

        score = (correct_answers_count / total_questions) * 100 if total_questions != 0 else 0

        data = {
            'total_questions': total_questions,
            'answered_questions': len(answered_questions),
            'correct_answers': correct_answers_count,
            'incorrect_answers': incorrect_answers_count,
            'score': score
        }

        return Response(data)