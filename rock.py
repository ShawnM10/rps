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


player1_name = raw_input("Enter player1 name: ")
player2_name = raw_input("Enter player2 name: ")

for x in range(3):
    choice1 = choice()
    print("{} chooses: {}!!".format(player1_name, choice1))
    choice2 = choice()
    print("{} chooses: {}!!".format(player2_name, choice2))
    compare(choice1, choice2)

print(" {} and {} thanks for playing!".format(player1_name, player2_name))
