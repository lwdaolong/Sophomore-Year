# Logan Wang 51603232

'''
 * Project#5 Columns
 * ICS 32A
 * 12/5/20
 * Handles view of Columns game
 * @author Logan Wang
'''
import pygame
import columns_logic


class ColumnsGame:
    def __init__(self):
        self._state = columns_logic.GameState(13,6,[])
        self._game_over = self._state.game_over

    def run(self) -> None:
        pygame.init()

        self._resize_surface((600, 600))

        clock = pygame.time.Clock()

        while self._game_over == False:
            self._game_over = self._state.game_over #update game over reference
            clock.tick(3) #TODO MODIFY FRAMERATE
            self._handle_events()
            self._redraw()

        pygame.quit()

    def _handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._end_game()
            elif event.type == pygame.VIDEORESIZE:
                self._resize_surface(event.size)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self._state.move_faller_left()
                if event.key == pygame.K_RIGHT:
                    self._state.move_faller_right()
                if event.key == pygame.K_SPACE:
                    self._state.rotate_faller()

        self._state.time_tick()



    def _redraw(self) -> None:
        surface = pygame.display.get_surface()

        surface.fill(pygame.Color(0, 183, 235)) #background color
        self._draw_blocks()

        pygame.display.flip()


    def _draw_blocks(self) -> None:
        for j in range(self._state.rows + 1):
            for i in range(len(self._state.game_board) - 1, -1, -1):
                self._draw_block(self._state.game_board[i][j], j, i)

    def _draw_block(self, val: str, row:int, col:int) -> None:
        #COLOR GUIDE
        """S = YELLOW, T = RED, V = Blue, W = Green
        X = Orange, Y =Purple, Z = Pink"""
        frac_x = (len(self._state.game_board)-1-col)/len(self._state.game_board)
        frac_y = row/len(self._state.game_board[1])

        #topleft_frac_x = frac_x - spot.radius() TODO REMOVE
        #topleft_frac_y = frac_y - spot.radius() TODO REMOVE

        frac_width = 1/len(self._state.game_board)
        frac_height = 1/len(self._state.game_board[1])

        surface = pygame.display.get_surface()
        width = surface.get_width()
        height = surface.get_height()

        topleft_pixel_x = frac_x * width
        topleft_pixel_y = frac_y * height

        pixel_width = frac_width * width
        pixel_height = frac_height * height

        #ASSIGN GEM COLOR
        gem_color = pygame.Color(0, 183, 235) #default is background color
        if 'S' in val:
            gem_color = pygame.Color(255, 255, 0) #Yellow
        elif 'T' in val:
            gem_color = pygame.Color(255, 0, 0) #Red
        elif 'V' in val:
            gem_color = pygame.Color(0, 0, 255) #Blue
        elif 'W' in val:
            gem_color = pygame.Color(0, 255, 0) #Green
        elif 'X' in val:
            gem_color = pygame.Color(255, 125, 0) #Orange
        elif 'Y' in val:
            gem_color = pygame.Color(125, 0, 255) #Purple
        elif 'Z' in val:
            gem_color = pygame.Color(255, 0, 255) #Pink


        pygame.draw.rect(
            surface, gem_color,
            pygame.Rect(
                topleft_pixel_x, topleft_pixel_y,
                pixel_width, pixel_height))

        pixel_center_x= topleft_pixel_x + pixel_width/2
        pixel_center_y = topleft_pixel_y + pixel_height / 2

        if '|' in val and val.count('|') == 2:
            attribute_color = pygame.Color(255, 255, 0) #Yellow
            pygame.draw.rect(
                surface, attribute_color,
                pygame.Rect(
                    pixel_center_x, pixel_center_y,
                    pixel_width / 4, pixel_height / 4))
        elif '*' in val:
            attribute_color = pygame.Color(0, 255, 0) #Green
            pygame.draw.rect(
                surface, attribute_color,
                pygame.Rect(
                    pixel_center_x, pixel_center_y,
                    pixel_width / 4, pixel_height / 4))





        #TODO DRAW ATTRIBUTE (falling, landed, frozen , matched, etc.

    def _end_game(self) -> None:
        self._game_over = True

    def _resize_surface(self, size: (int, int)) -> None:
        pygame.display.set_mode(size, pygame.RESIZABLE)

    def _on_mouse_button(self, pos: (int, int)) -> None:
        surface = pygame.display.get_surface()
        width = surface.get_width()
        height = surface.get_height()

        pixel_x, pixel_y = pos

        frac_x = pixel_x / width
        frac_y = pixel_y / height

        self._state.handle_click((frac_x, frac_y))


if __name__ == '__main__':
    ColumnsGame().run()
