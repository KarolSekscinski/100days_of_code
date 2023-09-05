from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        # window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        # canvas
        self.canvas = Canvas(width=300, height=250, background="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125,
                                                     text="Hello",
                                                     font=("Arial", 20, "italic"),
                                                     fill=THEME_COLOR
                                                     , width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # button
        right_button_img = PhotoImage(file="images/true.png")
        self.right_button = Button(image=right_button_img, highlightthickness=0, command=self.user_right)
        self.right_button.grid(column=0, row=2)

        false_button_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_button_img, highlightthickness=0, command=self.user_false)
        self.false_button.grid(column=1, row=2)

        # label
        self.score_label = Label(text="Score: 0", highlightthickness=0, background=THEME_COLOR, font=("Arial", 10), fg="white")
        self.score_label.grid(column=1, row=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score} ")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the game.")
            self.right_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def user_right(self):
        answer = self.quiz.check_answer("True")
        self.give_feedback(answer)

    def user_false(self):
        answer = self.quiz.check_answer("False")
        self.give_feedback(answer)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)


