from Question import Question
import time

question_promt = [
    "Who sang the title song for the latest Bond film, No Time to Die?\nAdele\nSam Smith\nBillie Eilish\n",
"\nWhich flies a green, white, and orange (in that order) tricolor flag?\nIreland\nIvory Coast\nItaly\n",
"\nWhat company makes the Xperia model of smartphone?\nSamsung\nSony\nNokia\n",
"\nWhich city is home to the Brandenburg Gate?\nVienna\nZurich\nBerlin\n"
]

questions = [
    Question(question_promt[0], "c"),
    Question(question_promt[1], "a"),
    Question(question_promt[2], "b"),
    Question(question_promt[3], "c")
]
quiz_length = len(questions)
def quiz_time(questions):
    score = 0
    for question in questions:
        answer = input(question.promt)
        time.sleep(0.1)
        if answer == question.answer:
            score += 1
    print("you got " + str(score) + "/" + str(quiz_length) + "correct")
    if score/quiz_length == 1:
        print("amazing!")
    elif score/quiz_length == 0:
        print("you're dogshit")

quiz_time(questions)