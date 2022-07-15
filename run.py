def print_rules():
    print("Pick a number to place 'X' on the board. Script will place 'O'. Your goal is to set three Xes in horizontal, vertical diagonal or diagonal line =)\n")
    print(" 1 | 2 | 3 ")
    print("---|---|---")
    print(" 4 | 5 | 6 ")
    print("---|---|---")
    print(" 7 | 8 | 9 \n")
def init_board():
    global board 
    board = ["X", " ", " ", " ", " ", " ", " ", " ", " ", " "]
def print_board(board):
    print("Board is: \n")
    print(f" {board[1]} | {board[2]} | {board[3]} ")
    print("---|---|---")
    print(f" {board[4]} | {board[5]} | {board[6]} ")
    print("---|---|---")
    print(f" {board[7]} | {board[8]} | {board[9]} \n")
def user_choice():
    correct=False
    while correct == False:
        i=input("Select board field (1-9)")
        if i not in ["1","2","3","4","5","6","7","8","9"]:
            print("Sorry, please type a number from 1 to 9")
        else:
            correct = True
    return int(i)
def update_user(field):
    global board
    board[field] = "X"
def script_turn():
    global board
    import random
    turn=0
    while turn == 0:
        x = random.randint(1,9)
        if board[x] == " ":
            turn=x
        else:
            pass
    board[turn]="O"
    print(f"cpu turn is {turn} board is {board}")
def check_win(board):
    global winner
    winner="none"
    if board[1]==board[2]==board[3]=="X" or board[4]==board[5]==board[6]=="X" or board[7]==board[8]==board[9]=="X" or board[1]==board[4]==board[7]=="X" or board[2]==board[5]==board[8]=="X" or board[3]==board[6]==board[9]=="X" or board[1]==board[5]==board[9]=="X" or board[3]==board[5]==board[7]=="X":
        winner="Player"
    elif board[1]==board[2]==board[3]=="O" or board[4]==board[5]==board[6]=="O" or board[7]==board[8]==board[9]=="O" or board[1]==board[4]==board[7]=="O" or board[2]==board[5]==board[8]=="O" or board[3]==board[6]==board[9]=="O" or board[1]==board[5]==board[9]=="O" or board[3]==board[5]==board[7]=="O":
        winner="CPU"
    elif " " not in board:
        winner="Draw"
    else:
        pass
def update_turn(last):
    return not last
def first_turn():
    global user_turn
    i="None"
    while i not in ["U", "C"]:
        i=input("Who is making first turn? User or CPU? Type U or C: ")
    return i=="U"
def win(winner):
    if winner == "Player":
        print("Congratulations! You win against incredible stupid CPU! ")
    elif winner == "Draw":
        print ("The best part about this game is that every time you play it, the outcomes will be totally different (mostly hilarious) and there is no wrong or right in this game.")
    else:
        print("I don't know how you did that, but you lost!")

print_rules()
init_board()
user_turn=first_turn()
print_board(board)
check_win(board)
print(f"{winner}")
while winner == "none":
    print(f"user turn: {user_turn}")
    if user_turn:
        print("User turn: \n")
        x=user_choice()
        update_user(x)
    else:
        print("CPU turn: \n ")
        script_turn()
    check_win(board)
    print_board(board)
    user_turn=update_turn(user_turn)
win(winner)