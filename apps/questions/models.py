from django.db import models

# Create your models here.
class Question(models.Model):
    question_id = models.IntegerField(unique=True)
    question_text = models.TextField()
    answer_text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_text
    
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    