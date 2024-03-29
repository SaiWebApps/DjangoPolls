from django.db import models

class Poll(models.Model):
    question = models.CharField(max_length=200)
    def _unicode_(self):
        return self.question;

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def _unicode_(self):
        return self.choice_text;