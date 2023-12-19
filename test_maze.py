import pytest
from exceptions import WrongCommandException
from solutions import Solution
from players import Player
from generators import Generator
from unittest.mock import Mock


def test_generating_maze_medium():
    # Проверяем, что при команде "Medium" сгенерируется лабиринт уровня binary
    generator = Generator(20, 20)
    generator.binary_generating = Mock()
    generator.generating_maze('Medium')
    generator.binary_generating.assert_called()


def test_generating_maze_hard():
    # Проверяем, что при команде "Hard" сгенерируется лабиринт уровня sidewinder
    generator = Generator(20, 20)
    generator.sidewinder_generating = Mock()
    generator.generating_maze('Hard')
    generator.sidewinder_generating.assert_called()


def test_generating_maze_wrong_command():
    # Проверяем, что при незнакомой команде функция выдаст WrongCommandException
    generator = Generator(20, 20)
    with pytest.raises(WrongCommandException):
        generator.generating_maze("qwerty")


def test_binary_generating_empty_line():
    # Провeряем, что у binary лабиринта будет пустой коридор сверху и справа
    generator = Generator(4, 4)
    field_up, field_right = generator.binary_generating()
    for i in range(len(field_up[0])):
        assert field_up[0][i] == 1
    for i in range(len(field_right)):
        assert field_right[i][-1] == 1


def test_sidewinder_generating_empty_line():
    # Провeряем, что у sidewinder лабиринта будет пустой коридор сверху
    generator = Generator(4, 4)
    field_up, field_right = generator.sidewinder_generating()
    for i in range(len(field_up[0])):
        assert field_up[0][i] == 1


def test_solution_maze_medium():
    # Проверяем, что при команде "Medium" вызовется функция решения binary лабиринта
    solution = Solution([], [])
    solution.binary_solution = Mock()
    solution.solution_maze("Medium", 20, 20)
    solution.binary_solution.assert_called()


def test_solution_maze_hard():
    # Проверяем, что при команде "Hard" вызовется функция решения sidewinder лабиринта
    solution = Solution([], [])
    solution.sidewinder_solution = Mock()
    solution.solution_maze("Hard", 20, 20)
    solution.sidewinder_solution.assert_called()


def test_solution_maze_wrong_command():
    # Проверяем, что при неизвестной команде функция решения выдаст WrongCommandException
    solution = Solution([], [])
    with pytest.raises(WrongCommandException):
        solution.solution_maze("qwerty", 20, 20)


def test_boundary_points_binary_solution():
    # Проверяем правильность решения лабиринта уровня binary в граничной точке
    field_up = [[1, 1, 1],
                [0, 0, 0],
                [0, 0, 0]]
    field_right = [[0, 0, 1],
                   [1, 1, 1],
                   [1, 1, 1]]
    solution = Solution(field_up, field_right)
    result = solution.binary_solution(2, 0)
    expected = ([], 2, 0)
    assert result == expected


def test_standart_binary_solution():
    # Проверяем правильность решения лабиринта уровня binary в обычной точке
    field_up = [[1, 1, 1, 1],
                [0, 0, 0, 0],
                [1, 1, 1, 0],
                [1, 1, 0, 0]]
    field_right = [[0, 0, 0, 1],
                   [1, 1, 1, 1],
                   [0, 0, 0, 1],
                   [0, 0, 1, 1]]
    solution = Solution(field_up, field_right)
    result = solution.binary_solution(1, 3)
    expected = ([(1, 3), (2, 3), (2, 2)], 3, 2)
    assert result == expected


def test_standart_sidewinder_solution():
    # Проверяем правильность решения лабиринта уровня sidewinder в обычной точке
    field_up = [[1, 1, 1, 1],
                [0, 0, 1, 0],
                [0, 1, 0, 0],
                [0, 1, 0, 0]]
    field_right = [[0, 0, 0, 1],
                   [1, 1, 0, 1],
                   [0, 1, 1, 1],
                   [1, 0, 1, 1]]
    solution = Solution(field_up, field_right)
    result = solution.sidewinder_solution(2, 3)
    expected = ([(2, 3), (2, 2), (2, 2), (2, 1), (2, 1), (3, 1), (3, 0)], 3, 0)
    assert result == expected


def test_boundary_points_sidewinder_solution():
    # Проверяем правильность решения лабиринта уровня sidewinder в граничной точке
    field_up = [[1, 1, 1],
                [1, 0, 0],
                [0, 0, 0]]
    field_right = [[0, 0, 1],
                   [0, 1, 1],
                   [1, 1, 1]]
    solution = Solution(field_up, field_right)
    result = solution.sidewinder_solution(1, 0)
    expected = ([], 1, 0)
    assert result == expected


def test_check_coordinates_standard():
    # Проверяем, что при равенстве координат конечной точки и координат игрока, функция выдает True
    player = Player(30, 60)
    player.rect.x, player.rect.y = 404, 404
    assert player.check_right_place(20, 20)


def test_check_coordinates_negative():
    # Проверяем, что при различии координат конечной точки и координат игрока, функция выдает False
    player = Player(30, 60)
    player.rect.x, player.rect.y = 403, 404
    assert not player.check_right_place(20, 20)
