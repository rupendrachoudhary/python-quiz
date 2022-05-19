class Quiz:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


question_list = [
    "Which sport Sachin belongs \n a) Football \n b) Cricket \n c) Tennis \n d) Hockey \n ",
    "Delhi is capital of \n a) India \n b) England \n c) USA \n d)Germany \n ",
    "Bikaner is in which state \n a) UP \n b) Bihar \n c) Rajasthan \n d) MP \n ",
    "Which one is a search engine \n a) Facebook \n b) Google \n c) Microsoft \n d) Whatsapp \n "
]

question_answer = [
    Quiz(question_list[0], "b"),
    Quiz(question_list[1], "a"),
    Quiz(question_list[2], "c"),
    Quiz(question_list[3], "b")

]


def user_score():
    global count
    count = 0
    for questions in question_answer:
        print(questions.question)
        user_answer = input("Enter your answer: ")
        if user_answer == questions.answer:
            count += 1

    return count


print(f"\nYour score is {user_score()}")



