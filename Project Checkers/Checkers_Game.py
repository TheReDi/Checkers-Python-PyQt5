import sys
from checkers import Ui_Checkers
from datetime import datetime
import traceback
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon  # Используется команда exec, что преобразовывает строку в код,
# поэтому Pycharm не видит, что QIcon нужен

WHITE = -1
BLACK = 1
LETTERS = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
LETTERS_R = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H'}


class Checkers(QMainWindow, Ui_Checkers):
    def __init__(self):
        super().__init__()
        self.history = []
        self.opponent = WHITE  # Цвет ходящего игрока
        self.selecting_figure, self.selecting_move = [], {}
        # Координаты фигур, которые могут ходить/ Координаты ходов, которые может осуществить фигура
        self.setupUi(self)  # Подключение UI
        self.buttons = [[self.A_1, self.A_2, self.A_3, self.A_4, self.A_5, self.A_6, self.A_7,
                         self.A_8], [self.B_1, self.B_2, self.B_3, self.B_4, self.B_5, self.B_6,
                         self.B_7, self.B_8],[self.C_1, self.C_2, self.C_3, self.C_4, self.C_5,
                         self.C_6, self.C_7, self.C_8], [self.D_1, self.D_2, self.D_3, self.D_4,
                         self.D_5, self.D_6, self.D_7, self.D_8],[self.E_1, self.E_2, self.E_3,
                         self.E_4, self.E_5, self.E_6, self.E_7, self.E_8], [self.F_1, self.F_2,
                         self.F_3, self.F_4,self.F_5, self.F_6,self.F_7, self.F_8],[self.G_1,
                         self.G_2, self.G_3, self.G_4, self.G_5, self.G_6, self.G_7, self.G_8],
                        [self.H_1, self.H_2, self.H_3, self.H_4, self.H_5, self.H_6, self.H_7,
                         self.H_8]]  # Список кнопок
        self.board = Board().board  # Подключение списочной доски
        self.Select_part_coord()  # Запуск функции нахождения фигур, которые могут ходить
        self.Back.clicked.connect(self.Back_move)
        # self.Menu.clicked.connect(self.Menu_Window)
        # self.Help.clicked.connect(self.Help_Window)
        self.Help.hide()
        self.Menu.hide()
        self.End_move.hide()
        for list_buttons in self.buttons:
            for button in list_buttons:
                button.clicked.connect(self.Checkers)  # Активирование функции Checkers
        self.choice_button = True  # Проверка отсутствия выбора фигуры. True - фигура НЕ выбрана
        self.part_coord = None  # Координаты фигуры, которой ходят

    def Checkers(self):
        try:
            action = []  # Состоит из функции фигуры, её начальное положение, её последнее положение
            # (При взятии добавляются значения: функция взятой фигуры, её положение)
            coord = LETTERS.get(self.sender().objectName().split('_')[0]), \
                    int(self.sender().objectName().split('_')[1]) - 1
            self.selecting_figure = set(self.selecting_figure)
            if self.choice_button:
                if coord not in self.selecting_figure:
                    pass
                else:
                    for i in self.selecting_figure:
                        if coord != i:
                            exec('self.' + LETTERS_R.get(i[0]) + '_' + str(i[1] + 1) +
                                 '.setIcon(QIcon("Image/' + self.board[i[0]][i[1]].char() +
                                 self.board[i[0]][i[1]].get_color()[1] + '.png"))')
                        else:
                            exec('self.' + LETTERS_R.get(i[0]) + '_' + str(i[1] + 1) +
                                 '.setIcon(QIcon("Image/' + self.board[i[0]][i[1]].char() +
                                 self.board[i[0]][i[1]].get_color()[1] + 'S.png"))')
                    for j in self.selecting_move.values():
                        if self.board[j[0]][j[1]] is None:
                            exec('self.' + LETTERS_R.get(j[0]) + '_' + str(j[1] + 1) +
                                 '.setIcon(QIcon(""))')
                    self.selecting_move = {}
                    self.part_coord = coord
                    self.part_coord_k = None
                    self.Select_move(coord)
                    self.choice_button = False
            else:
                action += self.board[self.part_coord[0]][self.part_coord[1]], self.part_coord, coord
                if coord not in self.selecting_figure and \
                        coord not in self.selecting_move.values():
                    self.choice_button = True
                    self.Select_part_coord()
                    for i in self.selecting_move.values():
                        exec('self.' + LETTERS_R.get(i[0]) + '_' + str(i[1] + 1) +
                             '.setIcon(QIcon(""))')
                elif coord not in self.selecting_move.values():
                    self.choice_button = True
                    self.Checkers()
                else:
                    self.choice_button = True
                    last_coord = coord
                    if abs(self.part_coord[0] - coord[0]) + abs(self.part_coord[1] - coord[1]) > 2:
                        while last_coord != self.part_coord:
                            for i in self.selecting_move.keys():
                                if len(i) == 3 and last_coord == i[0]:
                                    if self.board[i[1][0]][i[1][1]] is not None:
                                        if self.board[i[1][0]][i[1][1]].get_color()[1] == 'W':
                                            self.White.display(int(self.White.value()) - 1)
                                        elif self.board[i[1][0]][i[1][1]].get_color()[1] == 'B':
                                            self.Black.display(int(self.Black.value()) - 1)
                                    action.append([self.board[i[1][0]][i[1][1]], i[1]])
                                    exec('self.' + LETTERS_R.get(i[1][0]) + '_' + str(i[1][1] + 1) +
                                         '.setIcon(QIcon(""))')
                                    self.board[i[1][0]][i[1][1]] = None
                                    last_coord = i[2]
                                    break
                    exec('self.' + LETTERS_R.get(coord[0]) + '_' + str(coord[1] + 1) +
                         '.setIcon(QIcon("Image/' + self.board[self.part_coord[0]]
                         [self.part_coord[1]].char() +
                         str(self.board[self.part_coord[0]][self.part_coord[1]].get_color()[1]) +
                         '.png"))')
                    exec('self.' + LETTERS_R.get(self.part_coord[0]) + '_' + str(
                        self.part_coord[1] + 1)
                         + '.setIcon(QIcon(""))')
                    self.board[coord[0]][coord[1]] = self.board[self.part_coord[0]][
                        self.part_coord[1]]
                    self.board[self.part_coord[0]][self.part_coord[1]] = None
                    for i in self.selecting_move.values():
                        if coord != i:
                            exec('self.' + LETTERS_R.get(i[0]) + '_' + str(i[1] + 1) +
                                 '.setIcon(QIcon(""))')
                    if self.board[coord[0]][coord[1]].get_color()[1] == 'W' and \
                            coord[0] == 0:
                        self.board[coord[0]][coord[1]] = King(WHITE)
                        exec('self.' + LETTERS_R.get(coord[0]) + '_' + str(coord[1] + 1) +
                             '.setIcon(QIcon("Image/KW.png"))')
                    elif self.board[coord[0]][coord[1]].get_color()[1] == 'B' and \
                            coord[0] == 7:
                        self.board[coord[0]][coord[1]] = King(BLACK)
                        exec('self.' + LETTERS_R.get(coord[0]) + '_' + str(coord[1] + 1) +
                             '.setIcon(QIcon("Image/KB.png"))')
                    self.opponent = opponent(self.opponent)
                    self.Select_part_coord()
                    self.history.append(action)
                    if self.Black.value() == 0 or self.White.value() == 0:
                        exit()
        except Exception:
            now = str(datetime.now())
            y, mt, d, h, mn, s = now.split(' ')[0].split('-') + now.split(' ')[1].split(':')
            name = 'Logs/Log.{}.{}.{}.{}.{}.{}.txt'.format(d, mt, y, h, mn, s[:2])
            file = open(name, 'w')
            file.write('История ходов:\n\n' + str(self.history) + '\n\nОшибка:\n\n' +
                       traceback.format_exc() +
                       '\n\nВ случае обнаружения ошибки, пишите мне на почту: '
                       'albert.muhamet123@gmail.com . (Шанс ответа - 10 %)')
            exit()

    def Select_part_coord(self):
        self.selecting_figure = []
        point = self.opponent
        for row in range(8):
            for col in range(8):
                if self.board[row][col] and self.board[row][col].get_color()[0] == self.opponent:
                    cur_cor = correct_coordinates(row + point, col + point)
                    if not cur_cor[0] or not cur_cor[1]:
                        pass
                    elif self.board[row + point][col + point] is None:
                        exec("self." + self.buttons[row][col].objectName() +
                             '.setIcon(QIcon("Image/' + self.board[row][col].char() +
                             str(self.board[row][col].get_color()[1]) + 'S.png"))')
                        self.selecting_figure.append((row, col))
                    else:
                        cur_cor = correct_coordinates(row + (2 * point), col + (2 * point))
                        if not cur_cor[0] or not cur_cor[1]:
                            pass
                        elif self.board[row + (2 * point)][col + (2 * point)] is None and \
                                self.board[row + point][col + point].get_color()[0] != \
                                self.opponent:
                            exec("self." + self.buttons[row][col].objectName() +
                                 '.setIcon(QIcon("Image/' + self.board[row][col].char()
                                 + str(self.board[row][col].get_color()[1]) + 'S.png"))')
                            self.selecting_figure.append((row, col))
                    if 'King' in str(self.board[row][col]):
                        cur_cor = correct_coordinates(row - point, col + point)
                        if not cur_cor[0] or not cur_cor[1]:
                            pass
                        elif self.board[row - point][col + point] is None:
                            exec("self." + self.buttons[row][col].objectName() +
                                 '.setIcon(QIcon("Image/' + self.board[row][col].char() +
                                 str(self.board[row][col].get_color()[1]) + 'S.png"))')
                            self.selecting_figure.append((row, col))
                        else:
                            cur_cor = correct_coordinates(row - (2 * point), col + (2 * point))
                            if not cur_cor[0] or not cur_cor[1]:
                                pass
                            elif self.board[row - (2 * point)][col + (2 * point)] is None and \
                                    self.board[row - point][col + point].get_color()[0] != \
                                    self.opponent:
                                exec("self." + self.buttons[row][col].objectName() +
                                     '.setIcon(QIcon("Image/' + self.board[row][col].char()
                                     + str(self.board[row][col].get_color()[1]) + 'S.png"))')
                                self.selecting_figure.append((row, col))
                    cur_cor = correct_coordinates(row + point, col - point)
                    if not cur_cor[0] or not cur_cor[1]:
                        pass
                    elif self.board[row + point][col - point] is None:
                        exec("self." + self.buttons[row][col].objectName() +
                             '.setIcon(QIcon("Image/' + self.board[row][col].char() +
                             str(self.board[row][col].get_color()[1]) + 'S.png"))')
                        self.selecting_figure.append((row, col))
                    else:
                        cur_cor = correct_coordinates(row + (2 * point), col - (2 * point))
                        if not cur_cor[0] or not cur_cor[1]:
                            pass
                        elif self.board[row + (2 * point)][col - (2 * point)] is None and \
                                self.board[row + point][col - point].get_color()[0] != \
                                self.opponent:
                            exec("self." + self.buttons[row][col].objectName() +
                                 '.setIcon(QIcon("Image/' + self.board[row][col].char() +
                                 str(self.board[row][col].get_color()[1]) + 'S.png"))')
                            self.selecting_figure.append((row, col))
                    if 'King' in str(self.board[row][col]):
                        cur_cor = correct_coordinates(row - point, col - point)
                        if not cur_cor[0] or not cur_cor[1]:
                            pass
                        elif self.board[row - point][col - point] is None:
                            exec("self." + self.buttons[row][col].objectName() +
                                 '.setIcon(QIcon("Image/' + self.board[row][col].char() +
                                 str(self.board[row][col].get_color()[1]) + 'S.png"))')
                            self.selecting_figure.append((row, col))
                        else:
                            cur_cor = correct_coordinates(row - (2 * point), col - (2 * point))
                            if not cur_cor[0] or not cur_cor[1]:
                                pass
                            elif self.board[row - (2 * point)][col - (2 * point)] is None and \
                                    self.board[row - point][col - point].get_color()[0] != \
                                    self.opponent:
                                exec("self." + self.buttons[row][col].objectName() +
                                     '.setIcon(QIcon("Image/' + self.board[row][col].char() +
                                     str(self.board[row][col].get_color()[1]) + 'S.png"))')
                                self.selecting_figure.append((row, col))

    def Select_move(self, coord):
        row, col = coord
        point = self.opponent
        cur_cor = correct_coordinates(row + point, col + point)
        if not cur_cor[0] or not cur_cor[1]:
            pass
        elif self.board[row + point][col + point] is None:
            if self.part_coord == (row, col):
                exec("self." + self.buttons[row + point][col + point].objectName() +
                     '.setIcon(QIcon("Image/S.png"))')
                self.selecting_move[(row + point, col + point)] = (row + point, col + point)
        else:
            cur_cor = correct_coordinates(row + (2 * point), col + (2 * point))
            if not cur_cor[0] or not cur_cor[1]:
                pass
            elif self.board[row + (2 * point)][col + (2 * point)] is None and \
                    self.board[row + point][col + point].get_color()[0] != \
                    self.opponent and self.part_coord_k != (row + (2 * point), col + (2 * point)):
                exec("self." + self.buttons[row + (2 * point)][
                    col + (2 * point)].objectName() +
                     '.setIcon(QIcon("Image/S.png"))')
                self.selecting_move[(row + (2 * point), col + (2 * point)),
                                    (row + point, col + point), (row, col)] = \
                    (row + (2 * point), col + (2 * point))
                self.part_coord_k = row, col
                self.Select_move((row + (2 * point), col + (2 * point)))
        if 'King' in str(self.board[self.part_coord[0]][self.part_coord[1]]):
            cur_cor = correct_coordinates(row - point, col + point)
            if not cur_cor[0] or not cur_cor[1]:
                pass
            elif self.board[row - point][col + point] is None:
                if self.part_coord == (row, col):
                    exec("self." + self.buttons[row - point][col + point].objectName() +
                         '.setIcon(QIcon("Image/S.png"))')
                    self.selecting_move[(row - point, col + point)] = (row - point, col + point)
            else:
                cur_cor = correct_coordinates(row - (2 * point), col + (2 * point))
                if not cur_cor[0] or not cur_cor[1]:
                    pass
                elif self.board[row - (2 * point)][col + (2 * point)] is None and \
                        self.board[row - point][col + point].get_color()[0] != \
                        self.opponent and self.part_coord_k != \
                        (row - (2 * point), col + (2 * point)):
                    exec("self." + self.buttons[row - (2 * point)][
                        col + (2 * point)].objectName() +
                         '.setIcon(QIcon("Image/S.png"))')
                    self.selecting_move[(row - (2 * point), col + (2 * point)),
                                        (row - point, col + point), (row, col)] = \
                        (row - (2 * point), col + (2 * point))
                    self.part_coord_k = row, col
                    self.Select_move((row - (2 * point), col + (2 * point)))
        cur_cor = correct_coordinates(row + point, col - point)
        if not cur_cor[0] or not cur_cor[1]:
            pass
        elif self.board[row + point][col - point] is None:
            if self.part_coord == (row, col):
                exec("self." + self.buttons[row + point][col - point].objectName() +
                     '.setIcon(QIcon("Image/S.png"))')
                self.selecting_move[(row + point, col - point)] = (row + point, col - point)
        else:
            cur_cor = correct_coordinates(row + (2 * point), col - (2 * point))
            if not cur_cor[0] or not cur_cor[1]:
                pass
            elif self.board[row + (2 * point)][col - (2 * point)] is None and \
                    self.board[row + point][col - point].get_color()[0] != \
                    self.opponent and self.part_coord_k != (row + (2 * point), col - (2 * point)):
                exec("self." + self.buttons[row + (2 * point)][
                    col - (2 * point)].objectName() +
                     '.setIcon(QIcon("Image/S.png"))')
                self.selecting_move[(row + (2 * point), col - (2 * point)),
                                    (row + point, col - point), (row, col)] = \
                    (row + (2 * point), col - (2 * point))
                self.part_coord_k = row, col
                self.Select_move((row + (2 * point), col - (2 * point)))
        if 'King' in str(self.board[self.part_coord[0]][self.part_coord[1]]):
            cur_cor = correct_coordinates(row - point, col - point)
            if not cur_cor[0] or not cur_cor[1]:
                pass
            elif self.board[row - point][col - point] is None:
                if self.part_coord == (row, col):
                    exec("self." + self.buttons[row - point][col - point].objectName() +
                         '.setIcon(QIcon("Image/S.png"))')
                    self.selecting_move[(row - point, col - point)] = (row - point, col - point)
            else:
                cur_cor = correct_coordinates(row - (2 * point), col - (2 * point))
                if not cur_cor[0] or not cur_cor[1]:
                    pass
                elif self.board[row - (2 * point)][col - (2 * point)] is None and \
                        self.board[row - point][col - point].get_color()[0] != \
                        self.opponent and self.part_coord_k != \
                        (row - (2 * point), col - (2 * point)):
                    exec("self." + self.buttons[row - (2 * point)][
                        col - (2 * point)].objectName() +
                         '.setIcon(QIcon("Image/S.png"))')
                    self.selecting_move[(row - (2 * point), col - (2 * point)),
                                        (row - point, col - point), (row, col)] = \
                        (row - (2 * point), col - (2 * point))
                    self.part_coord_k = row, col
                    self.Select_move((row - (2 * point), col - (2 * point)))

    def Back_move(self):
        if not self.history:
            pass
        else:
            action = self.history[-1]
            part_coord = action[0]
            coord_primary = action[1]
            coord_last = action[2]
            if len(action) > 3:
                for take in action[3:]:
                    if take[0].get_color()[1] == 'W':
                        self.White.display(int(self.White.value()) + 1)
                    elif take[0].get_color()[1] == 'B':
                        self.Black.display(int(self.Black.value()) + 1)
                    exec('self.' + LETTERS_R.get(take[1][0]) + '_' + str(take[1][1] + 1) +
                         '.setIcon(QIcon("Image/' + take[0].char() + str(
                        take[0].get_color()[1]) + '.png"))')
                    self.board[take[1][0]][take[1][1]] = take[0]
            exec('self.' + LETTERS_R.get(coord_primary[0]) + '_' + str(coord_primary[1] + 1) +
                 '.setIcon(QIcon("Image/' + part_coord.char() + str(part_coord.get_color()[1]) +
                 '.png"))')
            exec('self.' + LETTERS_R.get(coord_last[0]) + '_' + str(coord_last[1] + 1) +
                 '.setIcon(QIcon(""))')
            self.board[coord_last[0]][coord_last[1]] = None
            self.board[coord_primary[0]][coord_primary[1]] = part_coord
            for i in self.selecting_figure:
                exec('self.' + LETTERS_R.get(i[0]) + '_' + str(i[1] + 1) +
                     '.setIcon(QIcon("Image/' + self.board[i[0]][i[1]].char() +
                     self.board[i[0]][i[1]].get_color()[1] + '.png"))')
            for j in self.selecting_move.values():
                if self.board[j[0]][j[1]] is None:
                    exec('self.' + LETTERS_R.get(j[0]) + '_' + str(j[1] + 1) +
                         '.setIcon(QIcon(""))')
            self.opponent = part_coord.get_color()[0]
            self.Select_part_coord()
            self.history.remove(action)

    def Menu_Window(self):  # Это так себе
        self.menu = Menu()
        self.menu.show()

    def Help_Window(self):  # А это пока в разработке ;)
        self.help = Help()
        self.help.show()

    def Restart(self):  # Тоже в разработке
        pass


class Help(QWidget):  # Все также в разработке
    def __init__(self):
        super().__init__()


class Menu(QWidget):  # Даже не пробуй запускать, не получится ))
    def __init__(self):
        super().__init__()


class Normal:
    def __init__(self, color):
        self.color = color

    @staticmethod
    def char():
        return 'N'

    def get_color(self):
        if self.color == WHITE:
            return self.color, 'W'
        else:
            return self.color, 'B'


class King:
    def __init__(self, color):
        self.color = color

    @staticmethod
    def char():
        return 'K'

    def get_color(self):
        if self.color == WHITE:
            return self.color, 'W'
        else:
            return self.color, 'B'


class Board:
    def __init__(self):
        self.board = [[None] * 8 for _ in range(8)]
        for col in range(1, 8, 2):
            for row in range(0, 3, 2):
                self.board[row][col] = Normal(BLACK)
            self.board[6][col] = Normal(WHITE)
        for col in range(0, 8, 2):
            for row in range(5, 8, 2):
                self.board[row][col] = Normal(WHITE)
            self.board[1][col] = Normal(BLACK)


def correct_coordinates(row, col):
    return 0 <= row <= 7, 0 <= col <= 7


def opponent(color):
    if color == WHITE:
        return BLACK
    else:
        return WHITE


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Checkers()
    ex.show()
    sys.exit(app.exec())
