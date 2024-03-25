x = 100 / 26
print(round(x, 3))
print(x)

list_ = [['*', '*'], [], []]

list_.clear()
list_.insert(0,['*', '*', '*'])
list_.insert(1,['*', '*', '*'])
list_.insert(2,['*', '*', '*'])
print(list_)

def draw_list_():
    for i in list_:
        print(*i)
    print()

print('----------------------------------------')

draw_list_()

def check_winner():
    if list_[0][0] == 'X' and list_[0][1] == 'X' and list_[0][2] == 'X':
        return 'X'
    if list_[1][0] == 'X' and list_[1][1] == 'X' and list_[1][2] == 'X':
        return 'X'
    if list_[2][0] == 'X' and list_[2][1] == 'X' and list_[2][2] == 'X':
        return 'X'
    if list_[0][0] == 'X' and list_[1][0] == 'X' and list_[2][0] == 'X':
        return 'X'
    if list_[0][1] == 'X' and list_[1][1] == 'X' and list_[2][1] == 'X':
        return 'X'
    if list_[0][2] == 'X' and list_[1][2] == 'X' and list_[2][2] == 'X':
        return 'X'
    if list_[0][0] == 'X' and list_[1][1] == 'X' and list_[2][2] == 'X':
        return 'X'
    if list_[0][2] == 'X' and list_[1][1] == 'X' and list_[2][0] == 'X':
        return 'X'
    if list_[0][0] == '0' and list_[0][1] == '0' and list_[0][2] == '0':
        return '0'
    if list_[1][0] == '0' and list_[1][1] == '0' and list_[1][2] == '0':
        return '0'
    if list_[2][0] == '0' and list_[2][1] == '0' and list_[2][2] == '0':
        return '0'
    if list_[0][0] == '0' and list_[1][0] == '0' and list_[2][0] == '0':
        return '0'
    if list_[0][1] == '0' and list_[1][1] == '0' and list_[2][1] == '0':
        return '0'
    if list_[0][2] == '0' and list_[1][2] == '0' and list_[2][2] == '0':
        return '0'
    if list_[0][0] == '0' and list_[1][1] == '0' and list_[2][2] == '0':
        return '0'
    if list_[0][2] == '0' and list_[1][1] == '0' and list_[2][0] == '0':
        return '0'
    return'*'


list_ = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]
print('Добро пожаловать в крестики-нолики')
print('----------------------------------')
draw_list_()
for i in range(1, 10):
    print(f'Ход: {i}')
    if i % 2 == 0:
        i_char = '0'
        print('Ходят нолики')
    else:
        i_char = 'X'
        print('Ходят крестики')
    row = int(input('Введите номер строки (1, 2, 3): ')) - 1
    column = int(input('Введите номер столбца (1, 2, 3): ')) - 1
    if list_[row][column] == '*':
        list_[row][column] = i_char
    else:
        print('Ячейка уже занята, вы пропускаете ход')
        draw_list_()
        continue

    draw_list_()

    if check_winner() == 'X':
        print('Победа крестиков')
        break
    if check_winner() == '0':
        print('Победа ноликов')
        break
    if check_winner() == '*' and i_char == 9:
        print('Ничья')
