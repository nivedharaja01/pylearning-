from question_model import Question
from data import question_data 
from quiz_brain import QuizBrain

question_bank = []
for quest in question_data:
    question_text = quest["text"]
    question_answer = quest["answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)

  
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
      quiz.next_question()

print("You've completed the quiz")
print(f"Your final score:{quiz.score}/{quiz.question_number}")
