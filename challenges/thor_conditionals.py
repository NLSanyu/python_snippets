#CodinGames Thor Conditionals Challenge

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]
current_x = initial_tx
current_y = initial_ty

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.
    
    difference_x = light_x - current_x 
    difference_y = light_y - current_y
    
    if difference_x  > 0:
        current_x += 1
        if difference_y > 0:
            move = 'SE'
            current_y += 1
        else:
            if difference_y < 0:
                move = 'NE'
                current_y -= 1
            else:
                move = 'E'
    else:
        if difference_x < 0:
            current_x -= 1
            if difference_y > 0:
                move = 'SW'
                current_y += 1
            else:
                if difference_y < 0:
                    move = 'NW'
                    current_y -= 1
                else:
                    move = 'W'
        else:
            if difference_y > 0:
                move = 'S'
                current_y += 1
            else:
                if difference_y < 0:
                    move = 'N'
                    current_y -= 1
                    
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    # A single line providing the move to be made: N NE E SE S SW W or NW
    print(move)