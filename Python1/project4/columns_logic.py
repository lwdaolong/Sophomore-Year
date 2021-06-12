#Logan Wang 51603232
'''
 * Project#4 Columns
 * ICS 32A
 * 11/19/20
 * Handles mechanics of Columns game
 * @author Logan Wang
'''
class GameState():

    def __init__(self,row:int,col:int,starting_board:[[str]]): #takes an argument of a 2d array of strings to represent
        #the starting 'CONTENTS' of the board. If an empty 2d list is given, then will create EMPTY board

        self.debug = False #TODO TURN OFF

        self.active_faller = None #should reference an instance of the Faller class
        self.rows = row
        self.cols =col
        self.game_over = False
        if(len(starting_board) >1):
            self.game_board = self.create_empty_board(self.rows, self.cols)
            self.set_up_contents(starting_board)
        else: #nothing in starting board, implying an empty board is wanted
            self.game_board = self.create_empty_board(self.rows, self.cols)


    def set_up_contents(self,starting_board:[[str]]) -> [[str]]:
        #uses a starting composition of jewels to set up the game board and allow the  jewels to fall naturally
        #assumes input of starting board is already transposed to match the game logic's board
        #also assumes that each element/jewel in the input is simply a single character
        for i in range(self.rows):
            for j in range(self.cols):
                self.game_board[i+1][j] = self._create_frozen_jewel(starting_board[i][j]) #[i+1] to offset sidewall
        self.level_game_board()
        return self.game_board

    def level_game_board(self)->None:
        #levels game board, filling in all 'holes'
        #use after matches jewels cleared
        #use in initial set up
        for i in range(1,self.rows+1,1):
            self._fill_col(self.game_board[i],self.rows)
        self.check_entire_board_matching()

    def _fill_col(self,column:[str], rows: int) ->None:
        #modifies a given column so that all jewel level out and fall to the bottom
        #also returns column
        while(self._room_to_fall(column,rows)):
            #while the last element in the column is blank, move all elements in the column down one space
            for i in range(rows): #work from bottom to top of column
                if(column[i] != self._create_empty_space() and
                column[i+1] == self._create_empty_space()):
                    column[i+1] =column[i]
                    column[i] = self._create_empty_space()
        return column

    def _room_to_fall(self, column:[str],rows:int) -> bool:
        room_to_fall = False
        for i in range(rows):
            if column[i] != self._create_empty_space() and column[i+1] == self._create_empty_space():
                room_to_fall = True
        return room_to_fall

    def create_empty_board(self, row: int, col: int) -> [['str']]:
        #creates an empty game board, board is transposed for easier movement and rotation calculations
        game_board = []
        game_board.append(self._create_side_wall(row))
        for i in range(col):
            game_board.append(self._create_empty_col(row))
        game_board.append(self._create_side_wall(row))
        return game_board

    def _create_empty_col(self, row:int) -> [str]:
        #only used in create_empty_board to make an empty column of the gameboard
        empty_col = []
        for i in range(row):
            empty_col.append(self._create_empty_space())
        empty_col.append(self._create_end_row())
        return empty_col

    def _create_side_wall(self, row:int) -> [str]:
        # returns a side wall of the board in the form of a list of strings
        wall_list =[]
        for i in range(row):
            wall_list.append('|')
        wall_list.append(' ') #makes a blank spot to avoid index out of bound errors when looking for diagonals
        return wall_list

    def _create_empty_space(self) ->str: #creates a string that symbolizes an empty space on the board
        return '   '

    def _create_frozen_jewel(self, char:str) ->str: #creates a string that symbolizes a frozen char on the board
        return f' {char} '

    def _create_faller_jewel(self, char:str) ->str: #creates a string that symbolizes a faller char on the board
        return f'[{char}]'

    def _create_landed_faller_jewel(self, char:str) ->str: #creates a string that symbolizes a landed faller char on the board
        return f'|{char}|'

    def _create_matching_jewel(self, char:str) ->str: #creates a string that symbolizes a matching char on the board
        return f'*{char}*'

    def _create_end_row(self) ->str: #creates a string that symbolizes an end row on the board
        return f'---'

    def draw_board(self): #draws game board in python shell
        for j in range(self.rows+1):
            for i in range(len(self.game_board) -1,-1,-1):
                print(self.game_board[i][j],end='')
            print()


    def quit(self) ->None: #sets game_over to True, effectively ending game
        self.game_over = True

    def game_over_method(self)->None: #if game naturally concludes, game over
        self.game_over = True
        print('GAME OVER')

    def create_faller(self, col:int, j1:str,j2:str,j3:str):
        if self.active_faller is None: #ensures one does not already exist
            faller = Faller(col,j1,j2,j3,self)
            if(self.game_board[faller.col][0] == self._create_empty_space()):
                self.active_faller = faller
                self.active_faller.fall()
            else:
                self.game_over_method()

    def time_tick(self):
        #passage of time, called when blank input given
        if self.active_faller is not None:
            temp_faller = self.active_faller
            temp_faller.fall()
            if '[' not in temp_faller.game_piece[0] and '|' not in temp_faller.game_piece[0]:
                self.check_entire_board_matching()
        else:
            self.clear_matching_jewels()
            self.check_entire_board_matching()
        #if matches and faller outside board, keep game going

    def rotate_faller(self):
        if self.active_faller is not None:
            self.active_faller.rotate_game_piece()

    def move_faller_left(self):
        if self.active_faller is not None:
            self.active_faller.move_left()

    def move_faller_right(self):
        if self.active_faller is not None:
            self.active_faller.move_right()


    def check_horizontal_matches_right(self, col: int, row:int, jewel_to_check: str, control_type:int) ->int or None:
        #takes in input of col and row, to specify from what start point in the board your are starting
        #to search for matches. Also takes in jewel_to_check for reference of what to match to.
        #takes in an int for control_type
        #if control_type ==0, checks for matches and returns an int of matches(not including the starting point)
        #if control_type ==1, actually draws matching pieces onto the game_board ex. ' A ' -> '*A*'
        if self.debug:
            print(f'CHECKING MATCHES HORIZONTAL LEFT: {col},{row}')
        sum_matches = 0
        col = col -1 #checks the one to the right,#only called internally, so no need to adjust col or row from user input
        row = row
        while(len(self.game_board[col][row]) >2 and
              len(jewel_to_check) > 2 and self.game_board[col][row][1] == jewel_to_check[1] and self.game_board[col][row] !=
        self._create_empty_space()):
            sum_matches+=1
            if(control_type ==1):
                self.game_board[col][row] = self._create_matching_jewel(jewel_to_check[1])
            col-=1
        return sum_matches

    def check_horizontal_matches_left(self, col: int, row:int, jewel_to_check: str, control_type:int) ->int or None:
        #takes in input of col and row, to specify from what start point in the board your are starting
        #to search for matches. Also takes in jewel_to_check for reference of what to match to.
        #takes in an int for control_type
        #if control_type ==0, checks for matches and returns an int of matches(not including the starting point)
        #if control_type ==1, actually draws matching pieces onto the game_board ex. ' A ' -> '*A*'
        if self.debug:
            print(f'CHECKING MATCHES HORIZONTAL RIGHT: {col},{row}')
        sum_matches = 0
        col = col + 1  # checks the one to the right,#only called internally, so no need to adjust col or row from user input
        row = row
        while (len(self.game_board[col][row]) >2 and
               len(jewel_to_check) > 2 and self.game_board[col][row][1] == jewel_to_check[1] and self.game_board[col][row] !=
        self._create_empty_space()):
            sum_matches += 1
            if (control_type == 1):
                self.game_board[col][row] = self._create_matching_jewel(jewel_to_check[1])
            col += 1
        return sum_matches

    def check_vertical_matches_up(self, col: int, row:int, jewel_to_check: str, control_type:int) ->int or None:
        #takes in input of col and row, to specify from what start point in the board your are starting
        #to search for matches. Also takes in jewel_to_check for reference of what to match to.
        #takes in an int for control_type
        #if control_type ==0, checks for matches and returns an int of matches(not including the starting point)
        #if control_type ==1, actually draws matching pieces onto the game_board ex. ' A ' -> '*A*'
        if self.debug:
            print(f'CHECKING MATCHES VERTICAL UP: {col},{row}')
        sum_matches = 0
        col = col   #only called internally, so no need to adjust col or row from user input
        row = row-1
        while( row >= 0):
            if (len(self.game_board[col][row]) >2 and
                    len(jewel_to_check) > 2 and
                    self.game_board[col][row][1] == jewel_to_check[1] and self.game_board[col][row] !=
        self._create_empty_space()):
                sum_matches += 1
                if (control_type == 1):
                    self.game_board[col][row] = self._create_matching_jewel(jewel_to_check[1])
                row -= 1
            else:
                break
        return sum_matches #high complexity, could be optimized later

    def check_vertical_matches_down(self, col: int, row:int, jewel_to_check: str, control_type:int) ->int or None:
        #takes in input of col and row, to specify from what start point in the board your are starting
        #to search for matches. Also takes in jewel_to_check for reference of what to match to.
        #takes in an int for control_type
        #if control_type ==0, checks for matches and returns an int of matches(not including the starting point)
        #if control_type ==1, actually draws matching pieces onto the game_board ex. ' A ' -> '*A*'
        if self.debug:
            print(f'CHECKING MATCHES VERTICAL DOWN: {col},{row}')
        sum_matches = 0
        col = col #only called internally, so no need to adjust col or row from user input
        row = row+1
        while (len(self.game_board[col][row]) >2 and
               len(jewel_to_check) > 2 and
               self.game_board[col][row][1] == jewel_to_check[1] and self.game_board[col][row] !=
        self._create_empty_space()):
            sum_matches += 1
            if (control_type == 1):
                self.game_board[col][row] = self._create_matching_jewel(jewel_to_check[1])
            row += 1
        return sum_matches

    def check_diagonal_matches_down_left(self, col: int, row:int, jewel_to_check: str, control_type:int) ->int or None:
        #takes in input of col and row, to specify from what start point in the board your are starting
        #to search for matches. Also takes in jewel_to_check for reference of what to match to.
        #takes in an int for control_type
        #if control_type ==0, checks for matches and returns an int of matches(not including the starting point)
        #if control_type ==1, actually draws matching pieces onto the game_board ex. ' A ' -> '*A*'
        if self.debug:
            print(f'CHECKING MATCHES DIAGONAL DOWN LEFT: {col},{row}')
        sum_matches = 0
        col = col + 1  #only called internally, so no need to adjust col or row from user input
        row = row +1    #checks first piece diagonal down left from start
        while (col < len(self.game_board) - 1 and row < len(self.game_board[col]) - 1):
            if (len(self.game_board[col][row]) >2 and
                    len(jewel_to_check) > 2 and self.game_board[col][row][1] == jewel_to_check[1] and self.game_board[col][
                row] !=
                    self._create_empty_space()):
                sum_matches += 1
                if (control_type == 1):
                    self.game_board[col][row] = self._create_matching_jewel(jewel_to_check[1])
                col += 1
                row += 1
            else:
                break
        return sum_matches

    def check_diagonal_matches_down_right(self, col: int, row:int, jewel_to_check: str, control_type:int) ->int or None:
        #takes in input of col and row, to specify from what start point in the board your are starting
        #to search for matches. Also takes in jewel_to_check for reference of what to match to.
        #takes in an int for control_type
        #if control_type ==0, checks for matches and returns an int of matches(not including the starting point)
        #if control_type ==1, actually draws matching pieces onto the game_board ex. ' A ' -> '*A*'
        if self.debug:
            print(f'CHECKING MATCHES DIAGONAL DOWN RIGHT: {col},{row}')
        sum_matches = 0
        col = col - 1  # only called internally, so no need to adjust col or row from user input
        row = row + 1  # checks first piece diagonal down right from start
        while( col >0 and row < len(self.game_board[col])-1):
            if (len(self.game_board[col][row]) >2 and
                    len(jewel_to_check) > 2 and self.game_board[col][row][1] == jewel_to_check[1] and self.game_board[col][row] !=
            self._create_empty_space()):
                sum_matches += 1
                if (control_type == 1):
                    self.game_board[col][row] = self._create_matching_jewel(jewel_to_check[1])
                col -= 1
                row += 1
            else:
                break
        return sum_matches

    def check_diagonal_matches_up_right(self, col: int, row:int, jewel_to_check: str, control_type:int) ->int or None:
        #takes in input of col and row, to specify from what start point in the board your are starting
        #to search for matches. Also takes in jewel_to_check for reference of what to match to.
        #takes in an int for control_type
        #if control_type ==0, checks for matches and returns an int of matches(not including the starting point)
        #if control_type ==1, actually draws matching pieces onto the game_board ex. ' A ' -> '*A*'
        if self.debug:
            print(f'CHECKING MATCHES DIAGONAL UP RIGHT: {col},{row}')
        sum_matches = 0
        col = col - 1  # only called internally, so no need to adjust col or row from user input
        row = row - 1  # checks first piece diagonal up right from start
        while (row >=0 and col >0):
            if (len(self.game_board[col][row]) >2 and
                    len(jewel_to_check) > 2 and self.game_board[col][row][1] == jewel_to_check[1] and self.game_board[col][row] !=
        self._create_empty_space()):
                sum_matches += 1
                if (control_type == 1):
                    self.game_board[col][row] = self._create_matching_jewel(jewel_to_check[1])
                col -= 1
                row -= 1
            else:
                break
        return sum_matches

    def check_diagonal_matches_up_left(self, col: int, row:int, jewel_to_check: str, control_type:int) ->int or None:
        #takes in input of col and row, to specify from what start point in the board your are starting
        #to search for matches. Also takes in jewel_to_check for reference of what to match to.
        #takes in an int for control_type
        #if control_type ==0, checks for matches and returns an int of matches(not including the starting point)
        #if control_type ==1, actually draws matching pieces onto the game_board ex. ' A ' -> '*A*'
        if self.debug:
            print(f'CHECKING MATCHES DIAGONAL UP LEFT: {col},{row}')
        sum_matches = 0
        col = col + 1  # only called internally, so no need to adjust col or row from user input
        row = row - 1  # checks first piece diagonal up left from start
        while (row >= 0 and col < len(self.game_board) - 1):
            if (len(self.game_board[col][row]) >2 and
                    len(jewel_to_check) > 2 and self.game_board[col][row][1] == jewel_to_check[1] and self.game_board[col][row] !=
        self._create_empty_space()):
                sum_matches += 1
                if (control_type == 1):
                    self.game_board[col][row] = self._create_matching_jewel(jewel_to_check[1])
            col += 1
            row -= 1
        return sum_matches

    def check_horizontal_matching(self,col:int,row:int,jewel_to_check:str)->bool:
        #checks both left and right horizontal matching
        #if a match of more than 3 is made, mark matches jewels
        sum =1
        sum+= self.check_horizontal_matches_left(col,row,jewel_to_check,0)
        sum+= self.check_horizontal_matches_right(col,row,jewel_to_check,0)
        if sum >= 3:
            self.check_horizontal_matches_left(col, row, jewel_to_check, 1)
            self.check_horizontal_matches_right(col,row,jewel_to_check,1)
            return True
        else:
            return False

    def check_vertical_matching(self,col:int,row:int,jewel_to_check:str)->bool:
        # checks both up and down horizontal matching
        # if a match of more than 3 is made, mark matches jewels
        sum =1
        sum+= self.check_vertical_matches_up(col,row,jewel_to_check,0)
        sum+= self.check_vertical_matches_down(col,row,jewel_to_check,0)
        if sum >= 3:
            self.check_vertical_matches_up(col,row,jewel_to_check,1)
            self.check_vertical_matches_down(col,row,jewel_to_check,1)
            return True
        else:
            return False

    def check_diagonal1_matching(self,col:int,row:int,jewel_to_check:str)->bool:
        # checks both upleft and downright diagonal matching '\'
        # if a match of more than 3 is made, mark matches jewels
        sum = 1
        sum += self.check_diagonal_matches_up_left(col, row, jewel_to_check, 0)
        sum += self.check_diagonal_matches_down_right(col, row, jewel_to_check, 0)
        if sum >= 3:
            self.check_diagonal_matches_up_left(col, row, jewel_to_check, 1)
            self.check_diagonal_matches_down_right(col, row, jewel_to_check, 1)
            return True
        else:
            return False

    def check_diagonal2_matching(self,col:int,row:int,jewel_to_check:str)->bool:
        # checks both upright and downleft diagonal matching '\'
        # if a match of more than 3 is made, mark matches jewels
        sum = 1
        sum += self.check_diagonal_matches_up_right(col, row, jewel_to_check, 0)
        sum += self.check_diagonal_matches_down_left(col, row, jewel_to_check, 0)
        if sum >= 3:
            self.check_diagonal_matches_up_right(col, row, jewel_to_check, 1)
            self.check_diagonal_matches_down_left(col, row, jewel_to_check, 1)
            return True
        else:
            return False

    def check_entire_board_matching(self):
        # checks each position on the board for matches and marks all matching jewels
        for i in range(1,len(self.game_board)-1,1):
            for j in  range(len(self.game_board[i]) -1):
                match_list = []
                match_list.append(self.check_horizontal_matching(i,j,self.game_board[i][j]))
                match_list.append(self.check_vertical_matching(i, j, self.game_board[i][j]))
                match_list.append(self.check_diagonal1_matching(i, j, self.game_board[i][j]))
                match_list.append(self.check_diagonal2_matching(i, j, self.game_board[i][j]))
                if True in match_list:
                    self.game_board[i][j] = self._create_matching_jewel(
                        self.game_board[i][j][1])  # only if one returns true

    def clear_matching_jewels(self):
        #clears matching jewels from the board
        for i in range(1, len(self.game_board) - 1, 1):
            for j in range(len(self.game_board[i]) - 1):
                if '*' in self.game_board[i][j]:
                    self.game_board[i][j] = self._create_empty_space()
        self.level_game_board()


class Faller():
    def __init__(self, col:int, j1: str, j2: str, j3:str, board: GameState):
        #takes in input of column the faller should start in, and three jewels with expected Strings for each jewel
        #creates data for a faller, but does not yet put it on the gameboard

        self.row = -1 #pointer of head of faller (bottommost element)
        # Starts at -1 because data exists outside gameboard
        self.game_board = board.game_board
        self.game_state = board
        self.game_piece =[self.game_state._create_faller_jewel(j1),
                          self.game_state._create_faller_jewel(j2),
                          self.game_state._create_faller_jewel(j3)]
        self.col = len(self.game_board) - col-1


    def fall(self)->None: #draws game pieces onto gameboard and makes piece fall
        if self.game_board[self.col][self.row+1]== self.game_state._create_empty_space():
            self.row +=1
            self.draw_faller()
            if self.game_board[self.col][self.row+1]!= self.game_state._create_empty_space():
                self.land_faller()
                self.draw_faller()
        else:
            if '[' in self.game_piece[0]: #ie if the piece is still 'falling'
                self.land_faller()
                self.draw_faller()
            elif '|' in self.game_piece[0]: #faller is landed and must bre frozen
                self.freeze_faller()
                self.draw_faller()
                self.game_state.active_faller = None #dereferences faller once its frozen

    def freeze_faller(self)->None:
        for i in range(len(self.game_piece)):
            self.game_piece[i] = self.game_state._create_frozen_jewel(self.game_piece[i][1])
        #TODO CHECK FOR MATCHES, allow game to keep going if matches made and faller not fully drawn
        #After checking for matches, if not all of the fall is on the screen, gameover
        if self.row +1 - len(self.game_piece) < 0:
            self.draw_faller()
            self.game_state.draw_board()
            self.game_state.game_over_method()

    def land_faller(self)->None:
        for i in range(len(self.game_piece)):
            self.game_piece[i] = self.game_state._create_landed_faller_jewel(self.game_piece[i][1])

    def fall_faller(self)->None:
        for i in range(len(self.game_piece)):
            self.game_piece[i] = self.game_state._create_faller_jewel(self.game_piece[i][1])

    def draw_faller(self)->None:
        for i in range(len(self.game_piece)-1,-1,-1):
            j= i-len(self.game_piece)+1+self.row
            if(j>=0):
                self.game_board[self.col][j] = self.game_piece[i]
                if (j - 1 >= 0):
                    self.game_board[self.col][j - 1] = self.game_state._create_empty_space()

    def rotate_game_piece(self)->None:
        #rotates a game piece by 1 unit
        #allowed if piece is not frozen
        if '[' in self.game_piece[0] or '|' in self.game_piece[0]:
            head = self.game_piece[len(self.game_piece)-1]
            for i in range(len(self.game_piece)-1,0,-1):
                self.game_piece[i] = self.game_piece[i-1]
            self.game_piece[0] = head
            self.draw_faller()

    def move_left(self)->None:
        #attempts to move the faller left one unit on the board
        #if space allows
        if(self.game_board[self.col+1][self.row] == self.game_state._create_empty_space()):
            self.erase_faller()
            self.col+=1
            self.draw_faller()
            if(self.game_board[self.col][self.row+1] == self.game_state._create_empty_space()):
                # if moving the faller causes it to have more room to fall, change back to brackets'[]'
                self.fall_faller()
                self.draw_faller()
            else:
                self.land_faller()
                self.draw_faller()
        #does nothing if no space available

    def move_right(self)->None:
        #attempts to move the faller right one unit on the board
        #if space allows
        if(self.game_board[self.col-1][self.row] == self.game_state._create_empty_space()):
            self.erase_faller()
            self.col-=1
            self.draw_faller()
        #does nothing if no space available
            if (self.game_board[self.col][self.row + 1] == self.game_state._create_empty_space()):
                # if moving the faller causes it to have more room to fall, change back to brackets'[]'
                self.fall_faller()
                self.draw_faller()
            else:
                self.land_faller()
                self.draw_faller()

    def erase_faller(self)->None:
        for i in range(len(self.game_piece)-1,-1,-1):
            j= i-len(self.game_piece)+1+self.row
            if(j>=0):
                self.game_board[self.col][j] = self.game_state._create_empty_space()
                if (j - 1 >= 0):
                    self.game_board[self.col][j - 1] = self.game_state._create_empty_space()

#assume board is at least 4 rows, 3 cols
#make pointer for faller that points to the bottom of the faller
#the logical game board is transposed to make for easier movement of fallers and rotations
