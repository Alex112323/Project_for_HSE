from exceptions import WrongCommandException


class Solution:

    def __init__(self, field_up, field_right):
        """Default constructor of Solution

        :param field_up: list of walls above
        :type field_up: list
        :param field_right: list of walls on the right
        :type field_right: list
        """
        self.field_up = field_up
        self.field_right = field_right

    def binary_solution(self, x, y):
        """Find solution of binary generating maze

        :param x: x-coordinate of current location
        :type x: int
        :param y: y-coordinate of current location
        :returns: right way to empty line and current coordinates
        """
        right_way = []

        # Проходим все точки, пока не попадем в пустые коридоры сверху или справа
        while y != 0 and x != len(self.field_up[0]) - 1:
            right_way.append((x, y))

            # Если отсутствует стенка сверху, поднимаемся
            if self.field_up[y][x] == 0:
                y -= 1

            # Если отсутствует стенка справа, идем направо
            elif self.field_right[y][x] == 0:
                x += 1

        return right_way, x, y

    def sidewinder_solution(self, x, y):
        """Find solution of sidewinder generating maze

        :param x: x-coordinate of current location
        :type x: int
        :param y: y-coordinate of current location
        :returns: right way to empty line and current coordinates
        """
        right_way = []

        # Проходим по всем точкам, пока не попадем в пустой коридор
        while y != 0:
            y1 = y
            x1 = x
            current_way = []

            # Ищем справа от текущей точки, есть ли точка с отстутствием стенки сверху
            while self.field_up[y][x] != 0 and self.field_right[y][x] == 0:
                current_way.append((x, y))
                x += 1
            if self.field_up[y][x] == 0:
                right_way.extend(current_way)
                right_way.append((x, y))
                right_way.append((x, y-1))
                y -= 1

            # Слева от текущей точки ищем, есть ли точка с отсутствием стенки сверху
            else:
                y = y1
                x = x1
                while self.field_up[y][x] != 0:
                    right_way.append((x, y))
                    x -= 1
                right_way.append((x, y))
                right_way.append((x, y - 1))
                y -= 1

        return right_way, x, y

    def solution_maze(self, command, x, y):
        """Return one of the maze solution functions

        :param command: level of game
        :type command: str
        :param x: x-coordinate of current location
        :type x: int
        :param y: y-coordinate of current location
        :type y: int
        :returns: binary solution if command = "Medium"
        :returns: sidewinder solution
        """

        # В зависимости от команды вызываем функцию решения лабиринта
        if command == "Medium":
            return self.binary_solution(x, y)
        elif command == "Hard":
            return self.sidewinder_solution(x, y)
        raise WrongCommandException
