"""
Tic Tac Toe game
Created by Bruce Barry

Here are the requirements:

-2 players should be able to play the game (both sitting at the same computer)
-The board should be printed out every time a player makes a move
-You should be able to accept input of the player position and then place a symbol on the board
"""
#Static Constants
WinningCombos=["123","147","159","258","357","369","456","789"]

#Variables
endProgram=False
keepAlive=True
cell=[1,2,3,4,5,6,7,8,9]
moves=[]
winningPlayer= None

player1= None
player2= None
player1Turn=True


# Functions for resetting games

def resetVaribles():
    """
used to reset the game but not the players names
"""
    global keepAlive
    keepAlive=True
    global cell
    cell=[1,2,3,4,5,6,7,8,9]
    global moves
    moves=[]
    global winningPlayer
    winningPlayer= None
    print("\n\n\nAll the settings are now reset except for the player names")

def restNames():
    """
resets the players to a new game
"""
    global player1
    player1= None
    global player2
    player2= None
    print("\n\n\nThe players have been reset")

#Functions that start the game

def yesNoRev(question):
    """
takes in the yes/no question and returns True/False BUT in this case the inverse bool
"""
    answer= input(question).lower()
    while not answer in ["yes","no"]:
        answer= input(question).lower()
    else:
        if answer == "yes":
            return False
        else:
            return True

def welcome():
    """
    This will:
    - introduce the game 
    - gathers the 2 players names
    - passes the name and piece of each player
    - prints the players information

    functions used:
    -namePlayer(player)
    -playerName()
    -xOrO()
    -antiStart()
"""
    print("Hello and welcome to the tic-tac-toe game!")
    print("You know the basic rules, connect any 3 connecting spaces and win. BUT LET'S BE HONEST, most games will end in a tie.\n\n")
    print("First we will take your names and the piece kind 'X' or 'O' with which you will be play. Then you will start the game.")
    print("To make a choice on where to move pick the number of the square you want to place your piece")

    global player1
    global player2
    if not player1:
        player1=namePlayer("first player!")
        player2=namePlayer("challenger!")
        antiStart()
    else:
        print("\n\n\n\nLooks like you are playing again")#for the second loop so you do not have to enter names every time

def playerName():
    """
Returns the players name
"""
    player=str(input("what is your name??? (only letters without any spaces or special characters please)"))
    while not player.isalpha():
        player= str(input("what is your name?"))
    return player.capitalize()

def xOrO(playerName):
    """
Takes in the players name and returns their piece assignment
"""
    piece= str(input(f"Hello {playerName}. Do you want to be an 'X' or an 'O'").upper())
    while not piece.isalpha() or piece not in ["X","O"]:
        piece= str(input(f"Hello {playerName}.Do you want to be an 'X' or 'O'???").upper())
    return piece

def namePlayer(player):
    """
    takes in a short message that is printed to identify the player

    it returns the players name and piece assignment
    """
    print("\n\n\nWelcome new and excited player! I know you are beyond excited to play so let us get this party going! You must be the",player)
    name= playerName()
    piece= None
    if not player1:
        piece= xOrO(name)
    else:
        other= player1[1]
        if other == "X":
            piece="O"
        elif other == "O":
            piece="X"
    return name,piece

def antiStart():
    """
Prints a few transition messages just before starting the main game loop
"""
    print("\n\nWell that settles it!",player1[0],"will go first and play as:",player1[1])
    print("\nAnd",player2[0],"will follow playing as:",player2[1])
    print("\n\nif you need further help please feel free to Google the rules.")
    print("Let's get to the game!")
    print(player1[0],"it is your board!")
    
    

#Game

def showBoard():
    """
    Will print the tic-tac-toe board every turn both at before a move and after
    """
    topBottom="+=====+=====+=====+"
    filler="|     |     |     |"
    frontCell="| "
    middleCell=" | "
    backCell=" |"
    
    def printTopRow():
        print(topBottom)
        print(filler)
        print(frontCell,cell[6],middleCell,cell[7],middleCell,cell[8],backCell)
        print(filler)
        print(topBottom)
    
    def printMidRow():
        print(filler)
        print(frontCell,cell[3],middleCell,cell[4],middleCell,cell[5],backCell)
        print(filler)
        print(topBottom)
        
    def printBotRow():
        print(filler)
        print(frontCell,cell[0],middleCell,cell[1],middleCell,cell[2],backCell)
        print(filler)
        print(topBottom)

    def pickInstructions():
        print("\n\nBelow you will see the board. Each of the 9 cells has a number that will need to be entered in order to claim that cell.")
        print("Any cell that has a number instead of 'X' or 'O' is open to be picked")


    printTopRow()
    printMidRow()
    printBotRow()

def avalibleCells():
    """
    Testing cell to return all the int enties that are legal moves
"""
    #test if int in for loop and append to list, return finished list
    xOrO= []
    number=[]
    for space in cell:
        if space == "O" or space == "X":    
            xOrO.append(space)
        else:
            number.append(space)
    left=8-len(xOrO)
    return number,left

def playerMove(firstTurn):
    """
    Asks for the player to choice an avalible cell.
    Decides player turn, requests players answer, tests if valid, and returns the T/F value to allow the next player to move

    I/O:
    I- T/F if player 1 is up
    O- the inverse value passed to function
"""
    if firstTurn:
        #player 1's turn
        player=player1[0]
        piece=player1[1]
        switch= False
    else:
        #player 2's turn
        player=player2[0]
        piece=player2[1]
        switch= True
    avalible, movesLeft= avalibleCells()
    choice= None
    while choice not in avalible:
        print(f"{player} it is your turn to place your {piece}")
        print(f"Any of these squares are avalibe:{avalible}")
        choice= int(input("\nWhere would you like to move?"))
    else:
        print("updating the board with your move")
        answer=[piece,choice] #creates a list of the piece and the cell location 
        moves.append(answer)
        loc=choice-1
        cell[loc]=piece
    
    if movesLeft >0:
        print("\n\n\n\n\n\n\n\nMOVESLEFT:",movesLeft)
        print(f"Here are the current moves made\n{moves}")
        return  switch
    else:
        global keepAlive
        keepAlive= False


def nameWinner(win):
    global winningPlayer
    win=int(win[0])-1
    result= moves[win][0]
    return result


def findWinner(x,o):
    """
used in winnerCheck() to iterate through each players choices to find if they have won
"""
    global winningPlayer
    for i in WinningCombos:
        if i in x or i in o:
            answer=nameWinner(i)
            if answer == player1[1]:
                winningPlayer= player1[0]
            else:
                winningPlayer= player2[0]
            return False
    else:
        return True

def winnerCheck():
    """
compares the board to all winning combinations to decide a winner
"""
    x=""
    o=""
    i=0
    #for loop checking list elements for
    for spot in cell:
        if spot == "X":
            x += str(i+1)
        elif spot == "O":
            o += str(i+1)
        i +=1
    #once x/o len =>3 check for winner
    count=len(x)+len(o)
    if count >4:
        print("\n\nchecking for a winner\n")
        killSwitch= findWinner(x,o)
        return True, killSwitch #return True(changes winner to True) and killswitch (T/F for keepAlive)
    else:
        return False, True
    
def game():
    """Main game loop, will run the game using keepAlive=True else will ask to exit or restart"""
    global player1Turn
    global keepAlive
    movesLeft= None
    winner=False
    
    
    while keepAlive:
        showBoard()#print board
        player1Turn= playerMove(player1Turn)#get player move
        winner, keepAlive=winnerCheck()#check if victory
        #Ask for another game
        #movesLeft()#check movesLeft
    else:
        if not winner:
            print("\n\n\nThis shit is over! Ends in a tie because of course it ends in a tie")
            showBoard()
        else:
            print(f"\n\n\nWE HAVE A WINNER!!! Congrads {winningPlayer} you have won the game!")
            showBoard()

def main():
    """
used to start the program and loop through it until the user requests to not play anymore
"""
    global endProgram
    while not endProgram:
        welcome() #Welcomes the players, ask for players name, and gives them X or O
        game()
        endProgram=yesNoRev("do you want to play again???(Yes or No)")
        resetVaribles()
    else:
        print("\n\n\nThank you for playing. Hopefully you enjoyed our time together!")
        x=input("\n\npress any key to quit")
main()
