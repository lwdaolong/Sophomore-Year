#Logan Wang 51603232
'''
 * Project#4 Columns
 * ICS 32A
 * 11/19/20
 * Tests basics of columns game logic
 * @author Logan Wang
'''
#project4_tester
import unittest
import columns_logic

class Project4Tester(unittest.TestCase):
    def setUp(self) -> None:
        self.test_board = columns_logic.GameState(4,3,[])

    def test_empty_space_string_creation(self):
        self.assertEqual(self.test_board._create_empty_space(),'   ')

    def test_frozen_jewel_string_creation(self):
        self.assertEqual(self.test_board._create_frozen_jewel('A'),' A ')

    def test_faller_jewel_string_creation(self):
        self.assertEqual(self.test_board._create_faller_jewel('A'),'[A]')

    def test_faller_landed_jewel_string_creation(self):
        self.assertEqual(self.test_board._create_landed_faller_jewel('A'),'|A|')

    def test_matched_jewel_string_creation(self):
        self.assertEqual(self.test_board._create_matching_jewel('A'),'*A*')

    def test_last_row_string_creation(self):
        self.assertEqual(self.test_board._create_end_row(),'---')

    def test_empty_create_empty_row(self):
        self.assertEqual(self.test_board._create_empty_col(0), ['---'])

    def test_general_create_empty_row(self):
        self.assertEqual(self.test_board._create_empty_col(4), ['   ','   ','   ','   ','---'])

    def test_empty_create_side_wall(self):
        self.assertEqual(self.test_board._create_side_wall(0), [' '])

    def test_general_create_side_wall(self):
        self.assertEqual(self.test_board._create_side_wall(4), ['|','|','|','|',' '])


    def test_regular_empty_board(self):
        self.assertEqual(self.test_board.game_board,[['|','|','|','|',' '],['   ','   ','   ','   ','---'],
                                                     ['   ','   ','   ','   ','---'],['   ','   ','   ','   ','---'],
                                                     ['|','|','|','|',' ']])

    def test_empty_empty_board(self):
        temp_test_board= columns_logic.GameState(0,0,[])
        self.assertEqual(temp_test_board.game_board,[[' '],[' ']])


    def test_room_to_fall_empty_column(self):
        self.assertEqual(self.test_board._room_to_fall(['   ','   ','   ','   ','---'],4),False)

    def test_room_to_fall_full_column(self):
        self.assertEqual(self.test_board._room_to_fall([' A ',' A ',' A ',' A ','---'],4),False)

    def test_room_to_fall_bottom_jewel(self):
        self.assertEqual(self.test_board._room_to_fall(['   ','   ','   ',' A ','---'],4),False)

    def test_room_to_fall_top_jewel(self):
        self.assertEqual(self.test_board._room_to_fall([' A ','   ','   ','   ','---'],4),True)

    def test_room_to_fall_mix(self):
        self.assertEqual(self.test_board._room_to_fall([' A ','   ',' A ',' A ','---'],4),True)

    def test_room_to_fall_mix2(self):
        self.assertEqual(self.test_board._room_to_fall([' A ','   ',' A ','   ','---'],4),True)

    def test_fill_col_empty(self):
        self.assertEqual(self.test_board._fill_col(['   ','   ','   ','   ','---'],4),['   ','   ','   ','   ','---'])

    def test_fill_col_bottom_jewel(self):
        self.assertEqual(self.test_board._fill_col(['   ','   ','   ',' A ','---'],4),['   ','   ','   ',' A ','---'])

    def test_fill_col_top_jewel(self):
        self.assertEqual(self.test_board._fill_col([' A ','   ','   ','   ','---'],4),['   ','   ','   ',' A ','---'])

    def test_fill_col_mix1(self):
        self.assertEqual(self.test_board._fill_col([' A ',' A ','   ','   ','---'],4),['   ','   ',' A ',' A ','---'])

    def test_fill_col_mix2(self):
        self.assertEqual(self.test_board._fill_col([' A ',' A ',' A ','   ','---'],4),['   ',' A ',' A ',' A ','---'])

    def test_fill_col_mix3(self):
        self.assertEqual(self.test_board._fill_col([' A ',' A ',' A ',' A ','---'],4),[' A ',' A ',' A ',' A ','---'])

    def test_fill_col_mix4(self):
        self.assertEqual(self.test_board._fill_col([' A ','   ',' A ',' A ','---'],4),['   ',' A ',' A ',' A ','---'])

    def test_fill_col_mix5(self):
        self.assertEqual(self.test_board._fill_col([' A ','   ','   ',' A ','---'],4),['   ','   ',' A ',' A ','---'])

    def test_fill_col_mix6(self):
        self.assertEqual(self.test_board._fill_col([' A ','   ',' A ','   ','---'],4),['   ','   ',' A ',' A ','---'])

    def test_fill_col_mix7(self):
        self.assertEqual(self.test_board._fill_col([' A ','   ','   ',' A ','---'],4),['   ','   ',' A ',' A ','---'])

    def test_starting_board_w_content(self):
        temp_test_board = columns_logic.GameState(4,4,[['X',' ','S','Y'],[' ','V','Y','X'],['Y',' ','X',' '],
                                                       [' ','S','T','X']])
        self.assertEqual(temp_test_board.game_board, [['|', '|', '|', '|', ' '], ['   ', ' X ', ' S ', ' Y ', '---'],
                                                      ['   ', ' V ', ' Y ', ' X ', '---'],
                                                      ['   ', '   ', ' Y ', ' X ', '---'],
                                                      ['   ', ' S ', ' T ', ' X ', '---'],
                                                      ['|', '|', '|', '|', ' ']])


    def test_faller_initialization(self):
        temp_test_faller = columns_logic.Faller(3,'x','y','z', self.test_board)
        self.assertEqual(temp_test_faller.row,-1)
        self.assertEqual(temp_test_faller.game_piece,['[x]','[y]','[z]'])



if __name__ == '__main__':
    unittest.main()
