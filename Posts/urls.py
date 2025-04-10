from django.urls import path
from Posts.views import QuestionListView, QuestionDetailView, QuestionCreateView, like_answer

urlpatterns = [
    path('', QuestionListView.as_view(), name='question_list'),
    path('question/<int:pk>/', QuestionDetailView.as_view(), name='question_detail'),
    path('question/new/', QuestionCreateView.as_view(), name='question_create'),
    path('answer/<int:pk>/like/', like_answer, name='like_answer'),
]