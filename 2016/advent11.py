#task = open('advent11.txt', 'r')

#pylint: disable=C0103

generators = {'H': 2, 'L': 3}
chips = {'H': 1, 'L': 1}
elevator = 1
floor_max = 4
capacity = 2


def show_el(code, floor):
    if code == 'E':
        if floor == elevator:
            return 'E'
    elif code[0] == 'F':
        return 'F' + str(floor)
    elif code[1] == 'M':
        if floor == chips[code[0]]:
            return code
    elif code[1] == 'G':
        if floor == generators[code[0]]:
            return code
    return '.'


def show():
    i = floor_max
    while i > 0:
        row = ''
        row += show_el('F', i) + '\t'
        row += show_el('E', i) + '\t'
        for j in chips:
            row += show_el(j + 'M', i) + '\t'
        for j in generators:
            row += show_el(j + 'G', i) + '\t'
        print(row)
        i -= 1
    print('\n')


def check_pos_ch(ch):
    possible = True
    if [chips, generators, elevator] in states:
        return False
    if chips[ch] > floor_max or chips[ch] <= 0:
        return False
    for g in generators:
        if chips[ch] == generators[g]:
            possible = False
        if chips[ch] == generators[ch]:
            possible = True
    return possible


def check_pos_g(gen):
    possible = True
    if [chips, generators, elevator] in states:
        return False
    if generators[gen] > floor_max or generators[gen] <= 0:
        return False
    for ch in chips:
        if chips[ch] == generators[gen]:
            possible = False
        if chips[gen] == generators[gen]:
            possible = True
    return possible

show()
state = [{}, {}]
state[0].update(chips)
state[1].update(generators)
state.append(elevator)
states = [state]
print states
while True:
    moves =[]
    for i in chips:
        move = False
        if chips[i] == elevator:
            chips[i] += 1
            if not check_pos_ch(i):
                chips[i] -= 1
            else:
                capacity -= 1
                moves.append(i + 'M' + '+')
                move = True
            if not move:
                chips[i] -= 1
                if not check_pos_ch(i):
                    chips[i] += 1
                else:
                    capacity -= 1
                    moves.append(i + 'M' + '-')

    for g in generators:
        move = False
        if generators[g] == elevator:
            generators[g] += 1
            if not check_pos_g(g):
                generators[g] -= 1
            else:
                capacity -= 1
                moves.append(g + 'G' + '+')
            if not move:
                generators[g] -= 1
                if not check_pos_g(g):
                    generators[g] -= 1
                else:
                    capacity -= 1
                    moves.append(g + 'G' + '-')
    if capacity < 2:
        elevator += int(moves[-1][-1])
        capacity = 2
    elif capacity == 2:
        print states
        chips = states[-2][0]
        generators = states[-2][1]
        elevator = states[-2][2]
        show()
        continue
    print(moves)
    show()
    state = [{}, {}]
    state[0].update(chips)
    state[1].update(generators)
    state.append(elevator)
    states.append(state)
    end = True
    for ch in chips:
        if chips[ch] != floor_max:
            end = False
            break
    for gen in generators:
        if generators[gen] != floor_max:
            end = False
            break
    if end:
        break
