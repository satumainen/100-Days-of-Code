from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

def get_question_data(question_data):
    question_bank = []
    for question in question_data:
        new_question = Question(question["question"], question["correct_answer"])
        question_bank.append(new_question)
    return question_bank


def main():
    quiz = QuizBrain(get_question_data(question_data))
    while quiz.still_has_questions():
        quiz.next_question()
    print(f"You have completed the quiz. Your final score was {quiz.score}/{quiz.question_number}")

main()


