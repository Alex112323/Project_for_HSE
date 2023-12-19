import random
import pygame
from players import Player
from generators import Generator
from drawings import Draw
from solutions import Solution

# Задаем параметры лабиринта
height = 30
width = 60
step = 20

# Создаем экземпляр генератора лабиринта
generator = Generator(height, width)

# Пользователь вводит уровень сложности
command = input("Please, write level (Medium or Hard): ")

# Если уровень сложности не соответсвует существующим, пользователь вводит заново
while command not in ["Medium", "Hard"]:
    print("We don't have " + command + " level")
    command = input("Please, write level (Medium or Hard): ")

screen = pygame.display.set_mode((generator.width * step, generator.height * step))

# Генерируем поля, отвечающие за наличие стены сверху и справа от клетки
field_up, field_right = generator.generating_maze(command)

pygame.init()
pygame.display.set_caption("Maze")
running = True

# Создаем экземпляр игрока
player = Player(height, width)

# Создаем экземпляр отрисовки
draw = Draw(screen, player, height, width)

# Задаем случайные координаты игрока
x, y = random.randrange(generator.width), random.randrange(generator.height)

flag = False

# Процесс игры
while running:

    # Создаем экземпляр решения в зависимости от полей стен сверху и снизу
    solution = Solution(field_up, field_right)

    # Генерируем пути от текущей и конечной точек до пустого коридора
    right_way_1, x1, y1 = solution.solution_maze(command, x, y)
    right_way_2, x2, y2 = solution.solution_maze(command, player.rect.x // step, player.rect.y // step)

    # Список всех нажатых пользователем кнопок
    keys = pygame.key.get_pressed()

    draw.drawing_maze(field_up, field_right, x, y, flag, right_way_1, x1, y1, right_way_2, x2, y2, command)
    pygame.display.update()

    # Обрабатываем все действия пользователя
    for event in pygame.event.get():

        # Обрабатываем движения игрока
        if keys[pygame.K_DOWN] and player.rect.y < generator.height * (step - 1):
            if field_up[player.rect.y // step + 1][player.rect.x // step] == 0:
                player.rect.y += step
        if keys[pygame.K_RIGHT] and field_right[player.rect.y // step][player.rect.x // step] == 0:
            player.rect.x += step
        if keys[pygame.K_LEFT] and player.rect.x > 0:
            if field_right[player.rect.y // step][player.rect.x // step - 1] == 0:
                player.rect.x -= step
        if keys[pygame.K_UP] and field_up[player.rect.y // step][player.rect.x // step] == 0:
            player.rect.y -= step

        # Создаем другой лабиринт по просьбе пользователя
        if keys[pygame.K_1] or keys[pygame.K_2]:
            if keys[pygame.K_1]:
                command = "Medium"
                field_up, field_right = generator.generating_maze(command)
            elif keys[pygame.K_2]:
                command = "Hard"
                field_up, field_right = generator.generating_maze(command)
            x, y = random.randrange(generator.width), random.randrange(generator.height)
            player.random_coordinates()
            flag = False

        # Проверяем, дошел ли игрок до конца, если нет - показываем решение
        if keys[pygame.K_RETURN]:
            if player.check_right_place(x, y):
                field_up, field_right = generator.generating_maze(command)
                x, y = random.randrange(width), random.randrange(height)
                player.random_coordinates()
                flag = False
            else:
                flag = True

        # Прерываем игру, если пользователь нажал соответствующую кнопку
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
