#Logan Wang 51603232
'''
 * Project#4 Columns
 * ICS 32A
 * 11/19/20
 * Handles Python shell UI & control of Columns Game
 * @author Logan Wang
'''
import columns_logic

def run_columns():
    #main input/output
    rows = int(input())
    cols = int(input())
    starting_board = translate_set_up_input(input(),rows,cols)
    game_board=columns_logic.GameState(rows,cols,starting_board)
    game_board.draw_board()
    while(game_board.game_over == False):
        handle_user_input(input(),game_board)
        if(game_board.game_over==False):
            game_board.draw_board()



def translate_set_up_input(user_input:str,rows:int,cols:int)->[[str]]:
    #translates set up input
    #if input is simply 'EMPTY', will return empty list
    #if input is CONTENTS, will ask for 'rows' more input and create a 2d list of strings
    translated_list = []
    if user_input == 'EMPTY':
        return translated_list
    if user_input == 'CONTENTS':
        for i in range(cols):
            translated_list.append([])
        for n in range(rows):
            temp_str = input()
            for j in range(cols-1,-1,-1):
                translated_list[j].append(temp_str[cols-1-j])
        return translated_list

def handle_user_input(user_input:str, game_board:columns_logic.GameState)->None:
    #Handles all user input
    if user_input == 'Q':
        game_board.quit()
    elif user_input =='':
        game_board.time_tick()
    elif user_input[0] == 'F':
        game_board.create_faller(int(user_input[2]),user_input[4],user_input[6],user_input[8]) #jank
    elif user_input =='R':
        game_board.rotate_faller()
    elif user_input =='<':
        game_board.move_faller_left()
    elif user_input =='>':
        game_board.move_faller_right()
if __name__ == '__main__':
    run_columns()


