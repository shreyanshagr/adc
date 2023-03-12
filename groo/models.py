from django.db import models

class NewUser(models.Model):
    username=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    password=models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.username

class Question(models.Model):
    question=models.CharField(max_length=255, blank=False, null=False)

    def __str__(self) -> str:
        return str(self.question)

class Answer(models.Model):
    question=models.ForeignKey(Question, on_delete=models.CASCADE)
    answer=models.CharField(max_length=255, blank=False, null=False)

    def __str__(self) -> str:
        return str(self.answer)
