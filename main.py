"""
name of the game is to get the most highest average amount of die numbers

if duplicate numbers are rolled then your turn is skiped

skipping a turn can let you get a bonus to your score
"""
print("THIS CODE IS MADE BY @zciplier on GITHUB || https://github.com/zciplier")
print("""
    _______            
  /\       \           
 /()\   ()  \          
/    \_______\      D I C E   
\    /()     /         
 \()/   ()  /          
  \/_____()/
""")
import random
import time
print("Welcome to a dice game player.\n")
print("This game is all about trying to get the highest average amount of dice")
print("If you get the same number through two turns, your third turn will get skipped.")
print("Skipping some turns might get you a bonus to target the other player...")
CPUorOTHERp = str(input("Would you like to play with another person (Y) or a CPU (N)? "))
turns = int(input("\nHow many turns shall each player be able to do? "))
placeholderturns = turns
if CPUorOTHERp == "Y":
    print("Alright player, thank you for choosing to play with another person.\n")
if CPUorOTHERp == "N":
    print("Alright player, thank you for choosing to play with a computer player.\n")
#other variables
bonus1 = 0
bonus2 = 0
totalscore1 = 0
totalscore2 = 0
FINALSCORE1 = 0
FINALSCORE2 = 0
winner = None
#currentplayer
class Player:
    def __init__(self, point, number, name, winner, total, finalscore):
        self.score = point
        self.turn = number
        self.whoami = name
        self.rank = winner
        self.total = total
        self.final = finalscore
#for each player
p1 = Player(0, 1, "Player 1", False, 0, 0)
p2 = Player(0, 2, "Player 2", False, 0, 0)
CPU = Player(0, 2, "CPU", False, 0, 0)
"""
two functions, one if there is a player and a cpu and another where there are two players

TURNA = CPU/PLAYER
TURNB = PLAYER/PLAYER

for loop that gets the input wether the CPUorOTHERp variable is set to play with another 
person or with a cpu

within the function, it adds the current user(s)/cpu's score to the player1/player2's
score array

BONUS information
when you skip your turn, you can get a chance to decrease the opponent's average score

every turn you skip, your amount increases to decrease the score

the numbers you can decrease it can go from 0 to 5
"""
#function to decrease the opponent's average score (AND ALSO ENDS THE GAME)
#b1 and b2 are the bonuses respective for each player
def end(playersorcpu, b1, b2, turnamount):
    #judging what is the winner of the game
    #add all of the scores together by average (mean)
    global win
    if playersorcpu == "N":
        if b1 > 0:
            CPU.total -= b1 % 2
        if p1.total / turnamount > CPU.total / turnamount:
            win = p1.whoami
        elif CPU.total / turnamount > p1.total / turnamount:
            win = CPU.whoami
        elif p1.total / turnamount == CPU.total / turnamount:
            win = p1.whoami + " and " + CPU.whoami
    elif playersorcpu == "Y":
        if b1 > 0:
            p2.total -= b1 / 2
        if b2 > 0:
            p1.total -= b2 / 2
        if p1.total / turnamount > p2.total / turnamount:
            win = p1.whoami
        elif p2.total / turnamount > p1.total / turnamount:
            win = p2.whoami
        elif p1.total / turnamount == p2.total / turnamount:
            win = p1.whoami + " and " + p2.whoami
    #bonus(s)
    if playersorcpu == "Y":
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("\nWelcome Player 1 and Player 2 to the end of the game.")
        print("The winner is")
        for i in range(4):
            print("." * i)
            time.sleep(1.5)
        print("\n" + win + " WINS!!\n")
        print("Scores: \n")
        print("Player 1 got: " + str(p1.total) + " points.")
        print("Player 2 got: " + str(p2.total) + " points.")
    elif playersorcpu == "N":
        print("\nWelcome player and CPU to the end of the game.")
        print("The winner is")
        for i in range(4):
            print("." * i)
            time.sleep(1.5)
        print("\n" + win + " WINS!!\n")
        print("Scores: \n")
        print("Player 1 got: " + str(p1.total) + " points.")
        print("The CPU got: " + str(CPU.total) + " points.")
"""
TURN WITH CPU
"""
def turnA(skip, p1choice1, p1choice2, cpuchoice1, cpuchoice2, bonus):
    #adds the player(s)/cpu's score to their respective array if skip isn't true
    if skip == False:
        p1.score = p1choice1 + p1choice2
        p1.total += p1.score
        print("Player 1 got " + str(p1choice1) + " and " + str(p1choice2) + ".")
        #this next line clears player 1's array, but leaves the scorep1 function
        #to save the total amount of score
        CPU.score = cpuchoice1 + cpuchoice2
        CPU.total += CPU.score
        print("Player 2 got " + str(cpuchoice1) + " and " + str(cpuchoice2) + ".")
    elif skip == True:
        #doesnt do what player 1 does and gives the bonus to player 1
        print("Player 1 might have got a bonus....\n")
        print("The CPU got " + str(cpuchoice1) + " and " + str(cpuchoice2) + ".")
        CPU.score = cpuchoice1 + cpuchoice2
        CPU.total += CPU.score
        bonus += 1

"""for loop that checks wether the "CPUorOTHERp" variable is equal to play with
a cpu or another player and then releases the functions based on those parameters

Y = another player
N = cpu player

"""
#function with second player
def turnB(skip1, skip2, p1choice1, p1choice2, p2choice1, p2choice2, bonus1, bonus2):
    #same as the past function
    """
    PLAYER1
    """
    #glorious if statements but their not if statements
    if skip1 == "N":
        p1.score = p1choice1 + p1choice2
        p1.total = p1.total + p1.score
        print("Player 1 got " + str(p1choice1) + " and " + str(p1choice2))
    if skip2 == "N":
        p2.score = p2choice1 + p2choice2
        p2.total = p2.total + p2.score
        print("Player 2 got " + str(p2choice1) + " and " + str(p2choice2))
    if skip1 == "Y":
        p2.score = p2choice1 + p2choice2
        p2.total = p2.total + p2.score
        bonus1 += 1
        print("Player 1 got " + str(p1choice1) + " and " + str(p1choice2))
        print("\nPlayer 1 might have got a bonus... ")
    if skip2 == "Y":
        p1.score = p1choice1 + p1choice2
        p1.total = p1.total + p1.score
        bonus2 += 1
        print("Player 2 is got " + str(p2choice1) + " and " + str(p2choice2))
        print("\nPlayer 2 might have got a bonus... ")
#MAIN FUNCTION LOOP THAT DOES EVERYTHING
for i in range(turns):
    print("\n\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    if turns > 1:
        print("You have " + str(turns) + " turns left to play.\n")
    elif turns == 1:
        print("You have " + str(turns) + " turn left to play.\n")
    #checks the variable to play with another player or a cpu
    """
    CPU WITH PLAYER
    """
    if CPUorOTHERp == "N":
        print(p1.whoami + " ,\n")
        skip = str(input("Would you like to skip this turn? [Y/N] "))
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        #function with parameters
        #if statement to check if skip is equal to either true or false
        if skip == "Y":
            #releases the function
            turnA(True, random.randint(0, 5), random.randint(0, 5), random.randint(0, 5), random.randint(0, 5), bonus1)
            print("\nPlayer 1 is at " + str(p1.total) + " points.")
            print("The CPU is at " + str(CPU.total) + " points.\n")
            turns -= 1 
        elif skip == "N":
            #releases the function again
            turnA(False, random.randint(0, 5), random.randint(0, 5), random.randint(0, 5), random.randint(0, 5), bonus1)
            print("\nPlayer 1 is at " + str(p1.total) + " points.")
            print("The CPU is at " + str(CPU.total) + " points.\n")
            turns -= 1
    """
    PLAYER WITH OTHER PLAYER
    """  
    if CPUorOTHERp == "Y":
        print(p1.whoami + " ,")
        skipp1 = input("Would you like to skip this round? [Y/N] ")
        print("\n" + p2.whoami + " ,")
        skipp2 = input("Would you like to skip this round [Y/N] ")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        #if statements
        turnB(skipp1, skipp2, random.randint(0, 5), random.randint(0, 5), random.randint(0, 5), random.randint(0, 5), bonus1, bonus2)
        print("\nPlayer 1 is at " + str(p1.total) + " points.")
        print("Player 2 is at " + str(p2.total) + " points.\n")
        turns -= 1
#end function that calculates everything"""
end(CPUorOTHERp, bonus1, bonus2, placeholderturns)
