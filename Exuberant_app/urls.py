from django.urls import path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('register/', Registration.as_view(), name='registration' ),
    path('logout/', Logout.as_view(), name='logout'),
    path('questions/', QuestionListCreateAPIView.as_view(), name='question-list-create'),
    path('answer/<int:pk>/', UserAnswerAPIView.as_view(), name='user-answer'),
    path('user/score/', UserTotalScoreAPIView.as_view(), name='user-score'),
]
