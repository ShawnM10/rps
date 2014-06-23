def choice():
    """returns choice in lowercase"""
    choice = raw_input("Enter a choice: ")
    return choice.lower()


def compare(choice1, choice2):
    """rock, paper, scissors"""
    if choice1 == choice2:
        print("It's a tie!")
    elif choice1 == 'rock':
        if choice2 == 'scissors':
            print('Rock wins!')
        elif choice2 == 'paper':
            print('Paper wins!')
    elif choice1 == 'paper':
        if choice2 == 'scissors':
            print('Scissors wins!')
        elif choice2 == 'rock':
            print('Paper wins!')
    elif choice1 == 'scissors':
        if choice2 == 'rock':
            print('Rock wins!')
        elif choice2 == 'paper':
            print('Scissors wins!')

for x in range(3):
    choice1 = choice()
    choice2 = choice()
    compare(choice1, choice2)
