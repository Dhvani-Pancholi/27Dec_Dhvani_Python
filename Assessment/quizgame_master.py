quiz_data = {}
questions = []
options = []
answers = []


def add_que(questions,options,answers):
    print("Added question:",questions)
    print("Option 1:",options)
    print("Option 2:",options)
    print("Answer:",answers)

def view_que(quiz_data):
    for que, data in quiz_data.items():
        print(f"Question: {que}")
        print(f"Options: {data['Options'][0]}, {data['Options'][1]}")
        print(f"Answer: {data['Answer']}")

def delete_que(questions):
    print("Deleted question:",questions)

def exit_que():
    print("Exit")
    
def cracker(add_que,score):
    print("Your Score is :",score)
    x = (print(add_que))
    print(x)    