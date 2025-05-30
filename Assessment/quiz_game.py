import quizgame_master as qm
from quizgame_master import *
import pandas

print("WELCOME TO TOPS QUIZ GAMING CHALLENGE")
print("""
select your role:
      1. Quiz master(press 1)
      2. Quiz cracker(press 2)
      3. Exit Application(press 3)
      """)
while True:
   role = int(input("Enter your role: "))

   if role == 1:
      print("-------Welcome Master----------")
      print("Shake your brain and add some challenging question")
      print("""
               MENU:
       press 1 for add question
       press 2 for view question
       press 3 for delete question
       press 4 for exit
         """)

   
      while True: 
         choice = int(input("Enter your choice(1,2,3,4):"))
         if choice == 1:
               seq = int(input("How many question you want to add? :"))
               print(seq)    
               for i in range(seq):
                     que = input("Your question is:")
                     print(que)
                     questions.append(que)
                     op1 = input("Enter option 1:")
                     options.append(op1)
                     print(op1)
                     op2 = input("Enter option 2:")
                     options.append(op2)
                     print(op2)
                     ans = input("Right answer:")
                     answers.append(ans)
                     print(ans)
                     quiz_data[que] = { "Options": [op1, op2], "Answer": ans}
                     print(quiz_data)
                     qm.add_que(questions, options, answers)  
         elif choice == 2:
            qm.view_que(quiz_data)
            result = pandas.DataFrame(quiz_data)
            print(result)
         elif choice == 3:
            del_serial_no = (input("Enter the  question to delete:"))
            if del_serial_no in quiz_data:
                del quiz_data[del_serial_no]
                print(f"Question {del_serial_no} deleted.")
            else:
                print("Invalid Question.")
         elif choice == 4:
               qm.exit_que()
               break
            

   elif role == 2:
      
                     print("-------Welcome Quiz Cracker----------")
                     score = 0
                     for question, data in quiz_data.items():
                       print(f"Question: {question}")
                       for idx in range(len(data["Options"])):
                         print(f"{idx + 1}. {data['Options'][idx]}")
                       answer = input("Enter the correct option number: ")
                       if data["Options"][int(answer) - 1] == data["Answer"]:
                         print("Correct!")
                         score += 1
                       else:
                         print("Wrong!")
                     qm.cracker(quiz_data,score)

                     print(f"Your final score is: {score}/{len(quiz_data)}")
                    
   elif role == 3:
      print("Existing the program")
      break                    
                     