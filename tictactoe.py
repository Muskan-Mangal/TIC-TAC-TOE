def check(l,marker):
    if(l[1]+l[2]+l[3]==marker*3 or l[4]+l[5]+l[6]==marker*3 or l[7]+l[8]+l[9]==marker*3 or l[1]+l[4]+l[7]==marker*3 or l[8]+l[5]+l[2]==marker*3 or l[9]+l[6]+l[3]==marker*3 or l[7]+l[5]+l[3]==marker*3 or l[9]+l[5]+l[1]==marker*3):
        return("won")
    elif(set(l)=={'o','x'} ):
        return("tie")
    else:
        return(False)
def display_board(l):
    print("          "+l[7]+'|'+l[8]+'|'+l[9])
    print('         --|-|--')
    print("          "+l[4]+'|'+l[5]+'|'+l[6])
    print('         --|-|--')
    print("          "+l[1]+'|'+l[2]+'|'+l[3])
def printer():
    print("                        WELCOME!!")
    print('RULES: You have to choose nos. from 1 to 9 to fill X or o at your desired positions and these numbers will be according to the standard numpad' )
    print('like this')
    board=['0','1','2','3','4','5','6','7','8','9']
    print("          "+str(board[7])+'|'+str(board[8])+'|'+str(board[9]))
    print('         --|-|--')
    print("          "+str(board[4])+'|'+str(board[5])+'|'+str(board[6]))
    print('         --|-|--')
    print("          "+str(board[1])+'|'+str(board[2])+'|'+str(board[3]))
    print("U R FIRST PLAYER,so first turn will be of yours")

def check_input(l,mark):
        if(l[int(mark)]!='o' and l[int(mark)]!='x' ):
            return True
        else:
            return False

print("                       TIC-TAC-TOE")
pl_agn='y'
while(pl_agn=='y'):
    printer()
    while(1):
        player1_marker =input("player1 CHOOSE EITHER 'x' OR 'o' AS YOUR MARKER: ")
        if(player1_marker=='x'):
            player2_marker='o'
            break
        if(player1_marker=='o'):
            player2_marker='x'
            break

    print(f'player1_marker is {player1_marker}')
    print(f'player2_marker is {player2_marker}')
    board=[0,' ',' ',' ',' ',' ',' ',' ',' ',' ']
    while(1):
        p1_mark=input(f'player1 enter the position at which u want to insert {player1_marker}: ')
        while(1):
            if(check_input(board,p1_mark)):
                board[int(p1_mark)]=player1_marker
                break
            else:
                print('sorry! But that position is already occupied')
                p1_mark=input(f'player1 again enter  the position other than this at which u want to insert {player1_marker}: ')
        display_board(board)
        if(check(board,player1_marker)=='won'):
            print("CONGRATES!!! You Won player1")
            print("U WANNA PLAY AGAIN?")
            pl_agn=input('if u wanna play agn,press y else press n')
            break
        elif(check(board,player1_marker)=='tie'):
            print("TIE")
            print("U WANNA PLAY AGAIN?")
            pl_agn=input('if u wanna play agn,press y else press n')
            break
        else:
            p2_mark=input(f'player2 enter the position at which u want to insert {player2_marker}: ')
            while(1):
                if(check_input(board,p2_mark)):
                    board[int(p2_mark)]=player2_marker
                    break
                else:
                    print('sorry! But that position is already occupied')
                    p2_mark=input(f'player2 again enter  the position other than this at which u want to insert {player2_marker}: ')
            display_board(board)
            if(check(board,player2_marker)=='won'):
                print("CONGRATES!!! You Won player2")
                print("U WANNA PLAY AGAIN?")
                pl_agn=input('if u wanna play agn press y else press n')
                break
            elif(check(board,player1_marker)=='tie'):
                print("TIE")
                print("YOU WANNA PLAY AGAIN?")
                pl_agn=input('If You wanna play agn press y else press n')
                break
