from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="question_by"
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="answer_by")
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="answer"
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="liked_answers", blank=True)

    class Meta:
        unique_together = ("question", "author")

    def __str__(self):
        return f"Answer by {self.author.username}"
