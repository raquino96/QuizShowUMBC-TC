#Quiz title
print(r"""
  ____                                                             _ _             
 / ___| _   _ _ __   ___ _ __   _ __ ___   ___  __ _  __ _   _   _| | |_ _ __ __ _ 
 \___ \| | | | '_ \ / _ \ '__| | '_ ` _ \ / _ \/ _` |/ _` | | | | | | __| '__/ _` |
  ___) | |_| | |_) |  __/ |    | | | | | |  __/ (_| | (_| | | |_| | | |_| | | (_| |
 |____/ \__,_| .__/ \___|_|    |_| |_| |_|\___|\__, |\__,_|  \__,_|_|\__|_|  \__,_|
             |_|                               |___/                               
   __                           _       _                      _ _ _ _ 
  / _|_   _ _ __     __ _ _   _(_)____ | |__   ___  _   _ _ __| | | | |
 | |_| | | | '_ \   / _` | | | | |_  / | '_ \ / _ \| | | | '__| | | | |
 |  _| |_| | | | | | (_| | |_| | |/ /  | | | | (_) | |_| | |  |_|_|_|_|
 |_|  \__,_|_| |_|  \__, |\__,_|_/___| |_| |_|\___/ \__,_|_|  (_|_|_|_)
                       |_|                                             
""")

#quiz rules
print("Time to answer some true or false questions. Please only answer 't' or 'f'.")
##question and answer tuples, var for iterator range, var for correct answer counter
questions = ( '1) Llamas are extinct.', '2) The mitochondria is the powerhouse of the cell.', '3) pluto is a planet (answer as if you were born before the year 2000).')
answers = ('f', 't', 't')
questionNum = len(questions)
correct = 0

#print question from tuple, create while loop to prompt user if invalid input is made, create if statement to check for correct answer and track number of correct statements 

for index in range(questionNum):
  print("")
  print(questions[index])
  userInput = input("Please enter 't' for true or 'f' for false: ")
  while userInput != 't' and userInput != 'f':
    userInput = input("Please enter 't' for true and 'f' for false: ")
   # if userInput == 't' or userInput == 'f':
    #  break
  if userInput == answers[index]:
    correct += 1
  #userInput = ""

print("")
print("""
  _ _ _  ____ ___  _   _  ____ ____      _  _____ _   _ _        _  _____ ___ ___  _   _ ____  _ _ _ 
 | | | |/ ___/ _ \| \ | |/ ___|  _ \    / \|_   _| | | | |      / \|_   _|_ _/ _ \| \ | / ___|| | | |
 | | | | |  | | | |  \| | |  _| |_) |  / _ \ | | | | | | |     / _ \ | |  | | | | |  \| \___ \| | | |
 |_|_|_| |__| |_| | |\  | |_| |  _ <  / ___ \| | | |_| | |___ / ___ \| |  | | |_| | |\  |___) |_|_|_|
 (_|_|_)\____\___/|_| \_|\____|_| \_\/_/   \_\_|  \___/|_____/_/   \_\_| |___\___/|_| \_|____/(_|_|_)
                                                                                                     
""")
print(f"you answered {correct} out of 3 correctly!")
if correct < 1:
  print("ehh.... we take back the 'congratulations'. Please go read a book or something. ")
  print("""
     ____ ___  _   _  ____ ____      _  _____ ____           
  / ___/ _ \| \ | |/ ___|  _ \    / \|_   _/ ___|          
 | |  | | | |  \| | |  _| |_) |  / _ \ | | \___ \          
 | |__| |_| | |\  | |_| |  _ <  / ___ \| |  ___) | _ _ _ _ 
  \____\___/|_| \_|\____|_| \_\/_/   \_\_| |____(_|_|_|_|_)

                       _           _          _             __
  _ __ ___  ___  ___(_)_ __   __| | ___  __| |    _      / /
 | '__/ _ \/ __|/ __| | '_ \ / _` |/ _ \/ _` |   (_)____| | 
 | | |  __/\__ \ (__| | | | | (_| |  __/ (_| |    |_____| | 
 |_|  \___||___/\___|_|_| |_|\__,_|\___|\__,_|   (_)    | | 
                                                         \_\
  """)



