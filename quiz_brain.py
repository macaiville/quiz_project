

class QuizBrain:
    def __init__(self, question_list):
        self.question_num = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_num]
        self.question_num +=1
        user_answer = input(f'Q.{self.question_num}: {current_question.text} (True/False)')
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        num_of_questions = len(self.question_list)
        if num_of_questions == self.question_num:
            print(f"Your score was {self.score}/{self.question_num}")
        if num_of_questions > self.question_num:
            return True
        else:
            return False
        
    
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right")
            self.score += 1
            print(f"Your current score is: {self.score}/{self.question_num}")
            print('/n')
        else:
            print("You got it wrong")
            print(f"Your current score is: {self.score}/{self.question_num}")
            print('\n')

        

