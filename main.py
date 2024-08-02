from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

#create an empty list called question_bank

#start a for loop, looping over each question in question_data

    #add a Question object as every element to the question_bank, like this: Question(question['text'], question['answer']), this is to be appended at the end of the list
    
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz!")
print(f"Your final score was {quiz.score}/{quiz.question_number}.")
