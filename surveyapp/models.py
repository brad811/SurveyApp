from django.db import models

class Question(models.Model):
    text = models.CharField(max_length=2048)
    creation_date = models.DateTimeField('date created', auto_now_add=True)
    def __str__(self):
        return str(self.pk) + " - " + self.text

class QuestionChoice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=2048)
    def __str__(self):
        num_votes = QuestionGuestResponse.objects.filter(question=self.question).filter(choice=self.pk).count()
        return "Question " + str(self.question.id) + ": " + self.text + " ("+str(num_votes)+" votes)"

class QuestionGuestResponse(models.Model):
    guest = models.CharField(max_length=2048)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(QuestionChoice, on_delete=models.CASCADE)
    def __str__(self):
        return "Question " + str(self.question.id) + ", Guest " + str(self.guest) + ", Choice: " + str(self.choice.id)
