from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from .models import Question

class QuestionView(APIView):
    def post(self, request):
        questions_num = request.data.get('questions_num', 1)
        questions = []

        for _ in range(questions_num):
            while True:
                response = requests.get('https://jservice.io/api/random?count=1')
                data = response.json()[0]

                question_id = data['id']
                question_text = data['question']
                answer_text = data['answer']

                if not Question.objects.filter(question_id=question_id).exists():
                    quiz_question = Question(
                        question_id=question_id,
                        question_text=question_text,
                        answer_text=answer_text
                    )
                    quiz_question.save()
                    questions.append({
                        'question_id': question_id,
                        'question_text': question_text,
                        'answer_text': answer_text,
                        'created_date': quiz_question.created_date
                    })
                    break

        return Response(questions, status=status.HTTP_201_CREATED)