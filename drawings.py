import pygame


class Draw:
    def __init__(self, screen, player, height, width):
        """Default constructor to create Draw

        :param screen: screen on which maze is displayed
        :type screen: pygame.surface.Surface
        :param player: player
        :type player: Player
        :param height: height of maze
        :type height: int
        :param width: width of maze
        :type width: int
        """

        self.height = height
        self.width = width
        self.player = player
        self.step = 20
        self.screen = screen

    def drawing_right_way(self, right_way_1, x1, y1, right_way_2, x2, y2, command):
        """Drawing right way from current location to final location

        :param right_way_1: list of points leading to an empty line from current location
        :type right_way_1: list
        :param x1: x-coordinate of current location on empty line
        :type x1: int
        :param y1: y-coordinate of current location on empty line
        :type y1: int
        :param right_way_2: list of points leading to an empty line from final location
        :type right_way_2: list
        :param x2: x-coordinate of final block location on empty line
        :type x2: int
        :param y2: y-coordinate of final block location on empty line
        :type y2: int
        :param command: level of game
        :type command: str
        :returns: None
        """
        # Создаем поверхность для отрисовки стены
        way = pygame.Surface((4, 4))
        way.fill("Green")

        # Отрисовываем путь от текущей точки до пустого коридора
        for i in range(len(right_way_1)):
            self.screen.blit(way, (right_way_1[i][0] * self.step + 10, right_way_1[i][1] * self.step + 10))

            # Проверяем пересечение с таким же путем от финальной точки
            if right_way_1[i] in right_way_2:
                break

        # Отрисовываем путь в пустом коридоре уровня "Medium"
        if command == "Medium":
            x1, x2 = min(x1, x2), max(x1, x2)
            for i in range(x1, x2):
                self.screen.blit(way, (i * self.step + 10, 10))
            y1, y2 = min(y1, y2), max(y1, y2)
            for i in range(y1, y2):
                self.screen.blit(way, ((self.width - 1) * self.step + 10, i * self.step + 10))

        # Отрисовываем путь в пустом коридоре уровня "Hard"
        if command == "Hard":
            x1, x2 = min(x1, x2), max(x1, x2)
            for i in range(x1, x2):
                self.screen.blit(way, (i * self.step + 10, 10))

        # Отрисовываем путь от финальной точки до пустого коридора
        for i in range(len(right_way_2)):
            self.screen.blit(way, (right_way_2[i][0] * self.step + 10, right_way_2[i][1] * self.step + 10))

            # Проверяем пересечение с таким же путем от текущей точки
            if right_way_2[i] in right_way_1:
                break

    @staticmethod
    def set_block_up():
        """Set blocks of walls and final block

        :returns: None
        """
        # Параметры стенки сверху
        block_up = pygame.Surface((20, 4))
        block_up.fill("Blue")

        # Параметры стенки справа
        block_right = pygame.Surface((4, 20))
        block_right.fill("Blue")

        # Параметры финальной точки
        final_block = pygame.Surface((12, 12))
        final_block.fill("Red")

        return block_up, block_right, final_block

    def drawing_maze(self, field_up, field_right, x, y, flag, right_way_1, x1, y1, right_way_2, x2, y2, command):
        """Drawing walls of maze

        :param field_up: list of walls above
        :type field_up: list
        :param field_right: list of walls on the right
        :type field_right: list
        :param x: x-coordinate of final block
        :type x: int
        :param y: y-coordinate of final block
        :type y: int
        :param flag: shows whether a solution is needed
        :type flag: bool
        :param right_way_1: list of points leading to an empty line from current location
        :type right_way_1: list
        :param x1: x-coordinate of current location on empty line
        :type x1: int
        :param y1: y-coordinate of current location on empty line
        :type y1: int
        :param right_way_2: list of points leading to an empty line from final block
        :type right_way_2: list
        :param x2: x-coordinate of final block on empty line
        :type x2: int
        :param y2: y-coordinate of final block on empty line
        :type y2: int
        :param command: level of game
        :type command: str
        :returns: None
        """
        self.screen.fill("Black")
        block_up, block_right, final_block = Draw.set_block_up()

        # Отрисовываем все игровое поле, просматривая наличие стен справа и сверху клетки
        for i in range(len(field_up)):
            for j in range(len(field_up[0])):
                if field_up[i][j] == 1:
                    self.screen.blit(block_up, (j * self.step, i * self.step))
                if field_right[i][j] == 1:
                    self.screen.blit(block_right, (j * self.step + 16, i * self.step))

        # Отрисовываем решение, если решение неправильное
        if flag:
            Draw.drawing_right_way(self, right_way_1, x1, y1, right_way_2, x2, y2, command)

        self.screen.blit(final_block, (x * 20 + 4, y * 20 + 4))
        self.screen.blit(self.player.image, self.player.rect)
        pygame.display.update()
