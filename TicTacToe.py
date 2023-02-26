#!/usr/bin/python3
# Script Name: TicTacToe.py
# Description: Simplified Tic Tac Toe game :-)
#              Tested on Linux, RHEL 8.5
# Usage: TicTacToe.py
# Author: CheerfulAnt@outlook.com
# Version: 1.0
# Date: 23 February 2022 - 21:00 (UTC+02:00)

import random
import os

board = [[1 ,2 ,3], [4, 5, 6], [7, 8, 9]]

comp_sign = "X"
user_sign = "O" 

def display_board(board):    

    for i in range(0, len(board)):
        print(" ", f"{'+--------':>9}" * 3, "+", sep="")
        print(" |", f"{'|':>8}", f"{'|':>8}", f"{'|':>8}")
        print(" |", f"{board[i][0]:^6}","|", f"{board[i][1]:^6}","|", f"{board[i][2]:^6}","|",)
        print(" |", f"{'|':>8}", f"{'|':>8}", f"{'|':>8}")
    print(" ", f"{'+--------':>9}" * 3, "+", sep="")
    
def user_move(board):

    user_value = input("Enter the field number: ")    
    if user_value == "q":
        print("So bye...")
        return 1
    else:
        try:            
            user_value = int(user_value)
            updated = 0
            if user_value >= 1 and user_value < 10:         
                for i in range(0, len(board)):    
                    for j in range(0, len(board[i])):
                        if board[i][j] == user_value:                            
                            board[i][j] = user_sign
                            updated += 1
                            return 3
                    if updated == 1:
                        break
                if updated == 0:
                    print()
                    print("Field number ", user_value, "is occupied! Try another number!")
                    print()                   
                    return 2                                 
            else:                    
                    return 4
        except:                                
                return 4
    
def make_list_of_free_fields(board):

    free_fields = []

    for i in range(0, len(board)):    
        for j in range(0, len(board[i])):
            if board[i][j] != comp_sign and board[i][j] != user_sign:                
                free_fields.append((i,j))
    return free_fields

def victory_for(board, sign):  
    
    sign = [ sign for i in range(len(board[0])) ]
    
    board_slash = []
    board_backslash = []
    board_slash_backslash = []
    is_winner = 0

    if board.count(sign):
        is_winner = 1

    for i in range(1, len(board) + 1):
            board_slash.append(board[i - 1][len(board) - i])
            board_backslash.append(board[i - 1][i - 1])

    board_slash_backslash.append(board_slash)
    board_slash_backslash.append(board_backslash)
    
    if board_slash_backslash.count(sign):
        is_winner = 1
            
    for i in range(1, len(board)):
        for j in range(i): 
            board[i][j], board[j][i] = board[j][i], board[i][j]
    
    if board.count(sign):
        is_winner = 1    

    for i in range(1, len(board)):
        for j in range(i): 
            board[i][j], board[j][i] = board[j][i], board[i][j]

    if is_winner == 1:
        return True
    else:
        return False             

def computer_move(board):
    if 5 in board[1]: #First move
        board[1][1] = "X"
    else:
        free_fields = make_list_of_free_fields(board)        
        comp_random_move = random.randrange(len(free_fields))
        free_one_field = free_fields[comp_random_move]
        board[free_one_field[0]][free_one_field[1]] = comp_sign
        
def welcome():
    print();
    print("Press \"q\" to quit.")
    print("Welcome in my simplified Tic Tac Toe game version 1.0 ;-)")
    print("The computer makes first move. Computer sign is X. User sign is O ;-)")
    print("Enter a unoccupied number from the table.")
    print();
        
os.system('clear')     

welcome()

computer_move(board)
display_board(board)

print();

while True:

        zw = user_move(board)

        if zw  == 1:
            break
        if zw  == 2:           
           welcome()
           display_board(board)           
           continue
        elif zw == 4:
            os.system('clear')
            welcome()
            display_board(board)
            print("Use only the fields numbers from 1 to 9...")
            continue
        else:
            os.system('clear')
            welcome()
            display_board(board)

        if victory_for(board, "O"):
            print("You won! Congratulations!:-)")
            break
        
        free_fields = make_list_of_free_fields(board)
        if len(free_fields) == 0:
            print("End of game! All fields filled! Draw!")
            break
        
        os.system('clear')
        welcome()
        print("Computer turn:")
        
        computer_move(board)
        
        display_board(board)

        if victory_for(board, "X"):
            print("Computer won! Don't give up, try one more time!:-)")
            break

        free_fields = make_list_of_free_fields(board)
        if len(free_fields) == 0:
            print("End of game! All fields filled! Draw!")
            break
