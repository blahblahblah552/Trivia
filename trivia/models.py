from django.db import models
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    category = models.CharField(max_length=40)

    def __str__(self):
        return self.category

class Question(models.Model):
    class Type(models.TextChoices):
        MULTIPLE_CHOICE = "Multiple Choice"
        TRUE_FALSE = "True or False"

    class Difficulty(models.TextChoices):
        EASY = "E", _("Easy")
        MEDIUM = "M", _("Medium")
        HARD = "H", _("Hard")

    true_or_false = models.BooleanField(default=False)

    difficulty = models.CharField(max_length=2, choices=Difficulty, default=Difficulty.MEDIUM)
    category = models.ManyToManyField(Category)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.question_text
    
class Choice(models.Model):
    question_ID = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=80)
    correct = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.correct:
            # Ensure that no other record has correct set to True
            Choice.objects.filter(correct=True).exclude(pk=self.pk).update(correct=False)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.choice_text

    
class User(models.Model):
    name = models.CharField(max_length=20)
    correctlyAnswered = models.PositiveIntegerField(default=0)
    incorrectlyAnswered = models.PositiveIntegerField(default=0)
