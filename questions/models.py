from django.db import models

# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Question(models.Model):
    DIFFICULTY_LEVELS = [
    ('Easy', 'Easy'),
    ('Medium', 'Medium'),
    ('Hard', 'Hard'),
    ]
    QUESTION_TYPES = [
    ('MCQ', 'Multiple Choice'),
    ('Short Answer', 'Short Answer'),
    ]
    text = models.TextField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_LEVELS)
    question_type = models.CharField(max_length=20,
        choices=QUESTION_TYPES)
    clo = models.CharField(max_length=10) # Course Learning Outcome
    def __str__(self):
        return self.text