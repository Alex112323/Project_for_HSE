import random
from exceptions import WrongCommandException


class Generator:
    def __init__(self, height, width):
        """Default constructor of Generator

        :param height: height of maze
        :type height: int
        :param width: width of maze
        :type width: int
        """
        self.height = height
        self.width = width
        self.ways = [[0] * self.width for _ in range(self.height)]

    def binary_generating(self):
        """Generating list of walls above and list of walls on the right by binary generating

        :returns: list of walls above and list of walls on the right
        """

        # Генерируем поле, имеющее все стены
        field_right = [[1] * self.width for _ in range(self.height)]
        field_up = [[1] * self.width for _ in range(self.height)]

        # В каждой клетке решаем случайно, убрать стену справа или сверху
        x, y = 0, 0
        while x < self.width and y < self.height:

            # Если мы не находимся в пустом коридоре, решаем случайно, где уберем стену
            if x < self.width - 1 and y >= 1:
                random_choice = random.randint(0, 1)
                if random_choice == 0:
                    field_right[y][x] = 0
                else:
                    field_up[y][x] = 0
                x += 1

            # Если находимся в пустом коридоре сверху, убираем стену справа
            elif y == 0 and x < self.width - 1:
                field_right[y][x] = 0
                x += 1

            # Если находимся в пустом коридоре справа, убираем стену снизу
            elif x == self.width - 1 and y != 0:
                field_up[y][x] = 0
                x = 0
                y += 1

            # Если находимся в крайней клетке справа сверху, никакую стену не убираем
            else:
                x = 0
                y += 1
        return field_up, field_right

    def sidewinder_generating(self):
        """Generating list of walls above and list of walls on the right by sidewinder generating

        :returns: list of walls above and list of walls on the right
        """
        # Генерируем поле, имеющее все стены
        field_right = [[1] * self.width for _ in range(self.height)]
        field_up = [[1] * self.width for _ in range(self.height)]

        x, y = 0, 0
        list_of_points = []

        # На каждом шаге решаем, добавить точку в список точек или рандомно убрать стенку сверху из списка точек
        while x < self.width and y < self.height:
            if x < self.width - 1 and y >= 1:
                random_choice = random.randint(0, 1)
                list_of_points.append((x, y))
                if random_choice == 0:
                    field_right[y][x] = 0
                else:
                    x1, y1 = random.choice(list_of_points)
                    list_of_points = []
                    field_up[y1][x1] = 0
                x += 1
            elif y >= 1:
                list_of_points.append((x, y))
                x1, y1 = random.choice(list_of_points)
                list_of_points = []
                field_up[y1][x1] = 0
                x = 0
                y += 1
            elif y == 0 and x < self.width - 1:
                field_right[y][x] = 0
                x += 1
            else:
                x = 0
                y = 1

        return field_up, field_right

    def generating_maze(self, command):
        """Return one of the maze generation functions

        :param command: level of game
        :type command: str
        :returns: binary generating function if command = "Medium"
        :returns: sidewinder generating function
        """
        # В зависимости от команды решаем, какой лабиринт сгенерировать
        if command == "Medium":
            return self.binary_generating()
        elif command == "Hard":
            return self.sidewinder_generating()

        raise WrongCommandException
