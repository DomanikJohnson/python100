class QuizBrain:
    def __init__(self,ilist):
        self.score = 0
        self.question_number = 0
        self.question_list = ilist

    def still_has_questions(self):
        if self.question_number <= len(self.question_list) - 1:
            return True
        return False


    def next_question(self):
        curr = self.question_list[self.question_number]
        self.question_number +=1
        ans = input(f" {self.question_number}: {curr.text} (True/False):   ")
        self.check_answer(ans, curr.answer)

    def check_answer(self, ians, correct_ians):
        if ians == correct_ians:
            self.score += 1
            print(f"Correct your Score is {self.score} / {self.question_number}")
        else:
            print(f"Incorrect answer: Score {self.score} / {self.question_number}")
        print("\n")

