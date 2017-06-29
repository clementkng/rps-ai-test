"""
Project: "Rock, Paper, Scissors!"

Developed by: Kunal Mishra, Jesse Luo, Jamie Delbick, Sathvik Nair, and Clement Ng  

Developed for: Beginning students in Computer Science

To run: python3 starter_RPS.py

Spec: https://goo.gl/cMvZfh

Student Learning Outcomes:
    Various levels of comfort with:
        small projects and abstraction
        understanding and modeling off existing code
        variables and lists
        functional programming
        loops and conditionals
        input/output
        artificial intelligence agents

Skill Level:
    assumed knowledge of language and concepts, but without mastery or even comfortability with them
    ~3-6 hours of experience/class/lecture necessary, coming into this project (for RPS) and 25-35 hours (for the AI extensions)
    ~Calibrated at well below the difficulty level of UC Berkeley's 61A project, Hog and somewhat below Paradigm Shift's Nifty project, "2048 in Python!"

Abstraction Reference Guide:
    main                    - responsible for starting and running the game
        name                - a variable inside main that contains the string of the user's name
        continue_playing    - a boolean variable within main that determines whether the game continues to another round
      
    Game Functions:
        play                - simulates one round of play 
        play_again          - returns "True" if user wants to play again and "False" if not
        determine_winner    - determines the winner between the user and computer based on each players' move 
    
    User Helper Functions:
        get_name            - gets user's name based on input
        move                - variable representing the user's move
        silent              - boolean used to print out steps of the game
    
    AI Functions:
        basic_ai            - ai function that randomly choices move
        ai_move             - variable representing the ai's move
        ai                  - represents the ai used in a round of the game 
"""
#basic_ai=""
import random

#End of first section
############################################################################################################
################################## DO NOT CHANGE ANYTHING ABOVE THIS LINE ##################################    - Section 2 -
############################################################################################################

#Start of Step 0 ###########################################################################################

def get_name():
    #Write out the prompt the user will see asking them to give the program their name
    prompt = ">>>>>>>>>>YOUR CODE HERE X<<<<<<<<<<"
    
    #Use a function to get the user's name (using the prompt)
    name = ">>>>>>>>>>YOUR CODE HERE X<<<<<<<<<<"

    #Return the name we "got" back to where this function was called
    return name

#End of Step 0 #############################################################################################



#Start of Step 1 ###########################################################################################

def play_again():
    # """Should be able to find whether the player wants to play again based on an input prompt
    
    # Run with python3 -m doctest -v starter_RPS.py < inputstep1.py
    # Feel free to change the prompts in the test to match your custom prompt. 
    # Need to comment out the other doctests in other steps to get this to work.
    
    # >>> play_again()
    # Want to play again? Starter
    # True
    # >>> play_again() 
    # Want to play again? Starter
    # False
    # >>> play_again() 
    # Want to play again? Starter
    # True
    # >>> play_again() 
    # Want to play again? Starter
    # False
    # >>> play_again() 
    # Want to play again? Starter
    # Invalid input!
    # <BLANKLINE>
    # Want to play again? Starter
    # False
    # """

    #Write out the prompt the user will see asking them whether they want to play again or not
    prompt = ">>>>>>>>>>YOUR CODE HERE X<<<<<<<<<<"
    
    #Use a function to get the user's choice (using the prompt)
    choice = ">>>>>>>>>>YOUR CODE HERE X<<<<<<<<<<"

    #Ensure the choice string is formatted properly (all lowercase letters)
    choice = ">>>>>>>>>>YOUR CODE HERE X<<<<<<<<<<"

    #If the choice was _____, the user wants to play again
    if ">>>>>>>>>>YOUR CODE HERE X<<<<<<<<<<":

        return True
    
    #If the choice was _____, the user does not want to play again
    elif ">>>>>>>>>>YOUR CODE HERE X<<<<<<<<<<":
        
        return False
    
    #If the choice was anything else, it wasn't valid input
    else:
        print("Invalid input!\n")
        return play_again()
        #Introduction to recursion! Ask a TA if you're curious as to how a function is calling itself!
        
#End of Step 1 #############################################################################################



#Start of Step 2 ###########################################################################################

def basic_ai():
    #The three possible moves, represented as strings
    moves = [">>>>>YOUR CODE HERE X<<<<<", ">>>>>YOUR CODE HERE X<<<<<", ">>>>>YOUR CODE HERE X<<<<<"]

    
    #Randomly select an index from moves
    index = ">>>>>>>>>>YOUR CODE HERE X<<<<<<<<<<"

    
    return moves[index]

#End of Step 2 #############################################################################################



#Start of Step 3 ###########################################################################################

def determine_winner(name, move, ai_move):
    assert ( (move    == "rock" or move    == "paper" or move    == "scissors") and 
             (ai_move == "rock" or ai_move == "paper" or ai_move == "scissors")
           ), "Wrong move or ai_move argument passed in"
    
    #Tie case
    if move == ai_move:
        return "Tie, no one wins!"
    
    #Win case 1
    elif ">>>>>>>>>>YOUR CODE HERE X<<<<<<<<<<":
        return name + " wins!"
    
    #Win case 2
    elif ">>>>>>>>>>YOUR CODE HERE X<<<<<<<<<<":
        return name + " wins!"
    
    #Win case 3    
    elif ">>>>>>>>>>YOUR CODE HERE X<<<<<<<<<<":
        return name + " wins!"
    
    #Losing case
    else:
        return ">>>>>>>>>>YOUR CODE HERE X<<<<<<<<<<"

#End of Step 3 #############################################################################################



#Start of Step 4 ###########################################################################################

def play(name, ai=basic_ai, silent=False):
    
    # """Method plays a single round of the game
    
    # # Run with python3 -m doctest -v starter_RPS.py < inputstep4.py
    # Feel free to change the prompts below to match your custom
    # Need to comment out the other doctests in other steps to get this to work.
    
    # >>> def rock_ai():
    # ...   moves = ["rock"]
    # ...   return moves[0]
    # >>> play('name', rock_ai)
    # Enter your move!
    # name plays rock
    # AI plays rock
    # Tie, no one wins!
    # 'Tie, no one wins!'
    # >>> play('name', rock_ai) 
    # Enter your move!
    # name plays scissors
    # AI plays rock
    # AI Player wins!
    # 'AI Player wins!'
    # >>> play('name', rock_ai, True) 
    # Enter your move!
    # 'name wins!'
    # """
    
    
    #Write out the prompt the user will see asking them to give the program their choice
    prompt = ">>>>>>>>>>YOUR CODE HERE X<<<<<<<<<<"
    
    #Use a function to get the user's move (using the prompt)
    move = ">>>>>>>>>>YOUR CODE HERE X<<<<<<<<<<"
    
    #Ensure the move is formatted properly (all lowercase letters)
    move = ">>>>>>>>>>YOUR CODE HERE X<<<<<<<<<<"

    #Get the AI's move
    ai_move = ai()
    
    #Use a functional abstraction to figure out who won -- the user or the AI
    winner = ">>>>>>>>>>YOUR CODE HERE X<<<<<<<<<<"

    #Check if the function is supposed to be silent or not -- print only if silent is False
    if ">>>>>>>>>>YOUR CODE HERE X<<<<<<<<<<":
        print(name + " plays " + move)
        print("AI plays " + ai_move)
        print(winner)
    
    return winner

#End of Step 4 #############################################################################################



#Start of Step 5 ###########################################################################################
        
def main():
    """Method works the main method
    
    Run with python3 -m doctest -v starter_RPS.py < inputstep5.py
    Need to get play and play_again working for this step to work.
    Feel free to change the prompts below to match your custom.
    Need to comment out the other doctests in other steps to get this to work.
    Due to limitations in determining AI's move (although you can try to make it
    deterministic), try to verify if your function is behaving correctly in the tests i.e. no exceptions
    See test 4 to see how might you write a deterministic AI to be able to predictively test this!
    
    >>> main()
    Enter your name: 
    Enter your move!
    name plays rock
    AI plays rock
    Tie, no one wins!
    Want to play again? Starter
    
    >>> main() 
    Enter your name: 
    Enter your move!
    name plays scissors
    AI plays rock
    AI Player wins!
    Want to play again? Starter
    Enter your move!
    name plays paper
    AI plays rock
    name wins!
    Want to play again? Starter
    """
    
    #Get the user's name
    name = ">>>>>>>>>>YOUR CODE HERE X<<<<<<<<<<"

    continue_playing = ">>>>>>>>>>YOUR CODE HERE X<<<<<<<<<<"

    while continue_playing:
        
        play(name)
        
        ontinue_playing = ">>>>>>>>>>YOUR CODE HERE X<<<<<<<<<<"

#End of Step 5 #############################################################################################

if __name__ == '__main__':
    import doctest
    doctest.testmod()


