class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def still_has_questions(self):
        """Returns boolean based on whether there are more questions in the question bank"""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """Prompts the user for the next quiz question"""
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Question {self.question_number}: {current_question.text} True or false?: ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        """Informs the user whether the answer is correct."""
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("Sorry, that was wrong.")
        print(f"The correct answer is {correct_answer}")
        print(f"Your score is {self.score}/{self.question_number}")
        print("\n")