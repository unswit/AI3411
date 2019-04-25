#!/usr/bin/python3

'''
COMP3411 19T1
Assignment 3 Nine-board Tic-Tac-Toe
Yiheng Quan Z5098268

I checked Zac senpai's starter code and got some ideas about what's going on.
My current solution to use minimax and alpha-beta pruning. Gradually increas ethe depth when the game is closer to an end.

The heuristic function will be measuring 'most wins' and the cost is always one for all moves.
'''

'''
init, start(), second_move(), third_move(),
last_move(), win(), loss(), draw(), end()
'''

import socket
import random
import sys

'''
9x9 board
0 - Empty
1 - Player
2 - Opponent
'''
game_boards = [[0] * 10 for i in range(10)]
curr_board = 0
player_name = 'Yiheng\'s AI Bot'

# print a row (modified from Zac senpai's code)
def print_row(board, a, b, c, i, j, k):
    # The marking script doesn't seem to like this either, so just take it out to submit
    print("", board[a][i], board[a][j], board[a][k], end = " | ")
    print(board[b][i], board[b][j], board[b][k], end = " | ")
    print(board[c][i], board[c][j], board[c][k])

# Print the entire board (modified from Zac senpai's code)
def print_board(board):
    print_row(board, 1,2,3,1,2,3)
    print_row(board, 1,2,3,4,5,6)
    print_row(board, 1,2,3,7,8,9)
    print(" ------+-------+------")
    print_row(board, 4,5,6,1,2,3)
    print_row(board, 4,5,6,4,5,6)
    print_row(board, 4,5,6,7,8,9)
    print(" ------+-------+------")
    print_row(board, 7,8,9,1,2,3)
    print_row(board, 7,8,9,4,5,6)
    print_row(board, 7,8,9,7,8,9)
    print()

# choose a move to play (modified from Zac senpai's code)
def play():
    # just play a random move for now
    n = random.randint(1,9)
    print("{0} {1}".format(curr_board, n))
    while game_boards[curr_board][n] != 0:
        n = random.randint(1,9)

    # print("playing", n)
    place(curr_board, n, 1)
    return n

# place a move in the global boards (modified from Zac senpai's code)
def place(board, num, player):
    global curr_board
    curr_board = num
    game_boards[board][num] = player

# Parse command from server (modified from Zac senpai's code)
def parse(string):
    if '(' in string:
        command, args = string.split('(')
        args = args.split(')')[0]
        args = args.split(',')
    else:
        command, args = string, []
    
    global player_name
    if command == 'second_move':
        player_name += ' O'
        place(int(args[0]), int(args[1]), 2)
        return play()
    elif command == 'third_move':
        player_name += ' X'
        # place the move that was generated for us
        place(int(args[0]), int(args[1]), 1)
        # place opponent's last move
        place(curr_board, int(args[2]), 2)
        return play()
    elif command == 'next_move':
        place(curr_board, int(args[0]), 2)
        return play()
    elif command == 'win':
        print('{} wins :)'.format(player_name))
        return -1
    elif command == 'loss':
        print('{} Lost :('.format(player_name))
        return -1
    return 0

# Setup socket and keep receiving commands (modified from Zac senpai's code)
def main():
    if (len(sys.argv) < 3 or (len(sys.argv) > 2 and not sys.argv[1] == '-p')):
        # some basic validations
        print('Usage: ./agent.py -p (port)')
        sys.exit(1)

    port = int(sys.argv[2])
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect(('localhost', port))
    while True:
        text = s.recv(1024).decode()
        if not text:
            continue
        for line in text.split('\n'):
            response = parse(line)
            # game is over
            if response < 0:
                s.close()
                return
            elif response > 0:
                s.sendall((str(response) + '\n').encode())

if __name__ == '__main__':
    main()