import random
print("If you have no more questions, say exit twice.")
def shake_ball():
    question = input("Ask a question: ")
    if(question == "exit"):
        return False
    responses = ["Yes definitely", "As I see it, yes", "Ask again later", "Cannot predict now", "Don't count on it", "Very doubtful", "Probably not", "Maybe", "Unlikely", "Definitely"]
    index = random.randint(0,9)
    print(responses[index])
    return True
while(shake_ball()):
    shake_ball()