from question_model import Question
import data
from quiz_brain import QuizBrain


qdatae = data.question_data
quiz_questions = []


for key in qdatae:
    quiz_questions.append(Question(key['text'], key['answer']))



quiz = QuizBrain(quiz_questions)

while quiz.still_has_questions():
        quiz.next_question()

print(f"Here is your score {quiz.score} ")