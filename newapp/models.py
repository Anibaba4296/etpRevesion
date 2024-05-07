

from django.db import models

# class VoteItem(models.Model):
#     name = models.CharField(max_length=100)
#     votes = models.IntegerField(default=0)

#     def __str__(self):
#         return self.name
class Question(models.Model):
    question_text = models.CharField(max_length=200)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)