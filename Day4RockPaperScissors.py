import random

rock = '''
     *  * 
  *        *  
 *          *  
 *          * 
  *        *  
     *  *      
'''
paper = '''
 ________ 
|        |
|        |
|        |
|________|
           
'''
scissors = '''
    _       ,/'
   (_).  ,/'
   __  ::
  (__)'  `\.
            `\.
'''
RPS = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))

CPU_rps = random.randint(0, 2)

if RPS == 0:
    print(rock)
elif RPS == 1:
    print(paper)
elif RPS == 2:
    print(scissors)
else:
    print("Number selected wasn't a 0, 1 or 2. You lose!")

if RPS > 2:
    print("")
elif CPU_rps == 0:
    print("The Computer chose: ")
    print(rock)
elif CPU_rps == 1:
    print("The Computer chose: ")
    print(paper)
elif CPU_rps == 2:
    print("The Computer chose: ")
    print(scissors)

if RPS == 0 and CPU_rps == 2:
    print("Player wins!")
elif RPS == 1 and CPU_rps == 0:
    print("Player wins!")
elif RPS == 2 and CPU_rps == 1:
    print("Player wins!")
elif RPS == 0 and CPU_rps == 0:
    print("It's a draw!")
elif RPS == 1 and CPU_rps == 1:
    print("It's a draw!")
elif RPS == 2 and CPU_rps == 2:
    print("It's a draw!")
elif RPS == 0 and CPU_rps == 1:
    print("You lost!")
elif RPS == 1 and CPU_rps == 2:
    print("You lost!")
elif RPS == 2 and CPU_rps == 0:
    print("You lost!")
