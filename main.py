from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


data = question_data
question_bank = []

for d in data:
    new_data = Question(d['text'], d['answer'])
    question_bank.append(new_data)



quiz = QuizBrain(question_bank)

while quiz.still_has_questions() == True:
    quiz.next_question()
    
