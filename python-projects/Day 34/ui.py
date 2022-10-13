from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#271736"
BG = "#edd3f5"


class QuizUI:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz")
        self.window.configure(padx=50, pady=50, background=THEME_COLOR)
        self.score_label = Label(text="Score: 0/0", foreground="white",font=("Helvetica", 20), background=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas(self.window, width=400, height=400, background=BG)
        self.question_label = self.canvas.create_text(200, 200, text="Question",width=300, font=("Helvetica", 16))
        self.canvas.grid(row=1, column=0, pady=30, columnspan=2)
        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(background=BG)
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_label, text=q_text)
        else:
            self.canvas.itemconfig(self.question_label, text="You've completed the quiz!")
            self.true_button.configure(state=DISABLED)
            self.false_button.configure(state=DISABLED)

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.configure(background="green")
        else:
            self.canvas.configure(background="red")
        self.score_label.configure(text="Score: " + str(self.quiz.score) + "/" + str(self.quiz.question_number))
        self.window.after(1000, self.get_next_question)



