from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")
score = 0

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain): #ensure object is of type QuizBrain
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR, padx=20, pady=20)

        self.canvas = Canvas(self.window, width=300, height=250, highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, text="", font=FONT, width=280)
        self.canvas.grid(row=1, column=0, sticky="nsew", columnspan=2, pady=50)

        self.score_label = Label(self.window, text=f"Score: {score}", font=("Arial", 15, "italic"), bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.true_pressed)
        self.true_button.config(padx=5, pady=5)
        self.true_button.grid(row=2, column=0, padx=20, pady=20)

        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_pressed)
        self.false_button.config(padx=5, pady=5)
        self.false_button.grid(row=2, column=1, padx=20, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        """Fetches the question from the quiz brain"""
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="Thank You For Playing!")
            self.true_button.config(state=DISABLED)
            self.false_button.config(state=DISABLED)

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))


    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))




    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
