from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from Posts.models import Question, Answer
from .forms import QuestionForm, AnswerForm
from django.shortcuts import redirect
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

@login_required
@require_POST
def like_answer(request, pk):
    answer = Answer.objects.get(pk=pk)
    if request.user in answer.likes.all():
        answer.likes.remove(request.user)
    else:
        answer.likes.add(request.user)
    return redirect("question_detail", pk=answer.question.pk)


class QuestionListView(ListView):
    model = Question
    template_name = "question_list.html"
    context_object_name = "questions"
    ordering = ["-updated_at"]


class QuestionCreateView(LoginRequiredMixin, CreateView):
    login_url = '/author/login/'
    
    model = Question
    form_class = QuestionForm
    template_name = "question_form.html"
    success_url = reverse_lazy("question_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class QuestionDetailView(LoginRequiredMixin, DetailView):
    login_url = '/author/login/'
    
    model = Question
    template_name = "question_detail.html"
    context_object_name = "question"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        question = self.get_object()
        user = self.request.user
        context["answers"] = question.answer.order_by("-created_at")
        context["answer_form"] = None
        context["already_answered"] = False

        if user.is_authenticated:
            if not question.answer.filter(author=user).exists():
                context["answer_form"] = AnswerForm()
            else:
                context["already_answered"] = True
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        question = self.object
        if request.user.is_authenticated and not question.answer.filter(author=request.user).exists():
            form = AnswerForm(request.POST)
            if form.is_valid():
                answer = form.save(commit=False)
                answer.question = question
                answer.author = request.user
                answer.save()
                messages.success(request, "Answer submitted successfully!")
            else:
                messages.error(request, "There was a problem submitting your answer.")
        return redirect("question_detail", pk=question.pk)

