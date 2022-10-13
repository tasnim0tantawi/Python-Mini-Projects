class QuizBrain:
    def __init__(self, question_list):
        self.question_index = 0
        self.question_list = question_list
        self.score = 0

    def still_has_question(self):
        return self.question_index < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_index]
        user_answer = input(f"Q. {self.question_index + 1}: {current_question.question} (True/ False)").lower()
        self.question_index += 1
        self.check_answer(user_answer, current_question.answer)
    def check_answer(self, u_answer, correct_answer):
        if u_answer == correct_answer:
            self.score += 1
            print("Correct! You got it right!")
            print(f"Your score is {self.score}/{self.question_index}")
        else:
            print(f"Wrong! The correct answer is {correct_answer}")
        print("-----------------------------------------------------")




