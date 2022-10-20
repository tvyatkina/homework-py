SHOW_ACTIONS = False # если поставить тру, то показывает все действия, делала для проверки
actions = 1

def remove_spaces(exp: str):
    exp_list = list(exp)
    i = 0
    while i < len(exp_list):
        if exp_list[i] == ' ':
            del exp_list[i]
            i -= 1
        i += 1
    return ''.join(exp_list)

def div(a: float, b: float):
    if b != 0:
        return a / b
    else:
        print(f'Ошибка: деление на ноль ({a}/{b})')
        exit()

def get_bracket(exp: str):
    count_of_brackets = 0
    have_brackets = False

    first_ind = -1

    func = None
    for ind, elem in enumerate(exp):
        if elem == '(':
            count_of_brackets += 1
            if not have_brackets:
                have_brackets = True
                first_ind = ind

        elif elem == ')':
            count_of_brackets -= 1
        if count_of_brackets == 0 and have_brackets:
            last_ind = ind
            if func:
                func_elems = exp[first_ind+1:last_ind]
                if len(func_elems) > 1:
                    ind_del = len(func_elems[0])
                    return first_ind, first_ind + ind_del + 1, (func, func_elems[1:]), last_ind
            return first_ind, last_ind, (func, None), last_ind
    return

def processing_plus_minus(exp: str) -> str:
    elems_split = ['-', '+']
    elems_split_mul = ['/', '*', 'х', ':']
    split_e = 'e'
    func = {'-': float.__sub__, '+': float.__add__}
    groups = []
    signs = []
    if exp[0] in elems_split:
        exp = '0'+exp

    last_ind = -1
    for ind, elem in enumerate(exp):
        if elem in elems_split and exp[ind-1] not in elems_split_mul \
                and exp[ind-1] not in elems_split and exp[ind-1] != split_e:
            groups.append(exp[last_ind+1:ind])
            signs.append(elem)
            last_ind = ind
    if last_ind == -1:
        groups.append(str(processing_mul_div(exp)))
    else:
        groups.append(exp[last_ind + 1:])

    for i in signs:
        tmp1 = processing_mul_div(groups[0])
        tmp2 = processing_mul_div(groups[1])

        groups[0] = str(func[i](tmp1, tmp2))

        if SHOW_ACTIONS:
            global actions
            print(f'{actions}) {tmp1} {i} {tmp2} = {groups[0]}')
            actions += 1

        del groups[1]
    return groups[0]

def processing_mul_div(exp: str) -> float:
    elems_split = ['/', '*', 'х', ':']
    func = {'/': div, ':': div, '*': float.__mul__, 'х': float.__mul__}
    groups = []
    signs = []

    last_ind = -1
    for ind, elem in enumerate(exp):
        if elem in elems_split:
            groups.append(exp[last_ind + 1:ind])
            signs.append(elem)
            last_ind = ind
    if last_ind == -1:
        groups.append(float(exp))
    else:
        groups.append(exp[last_ind + 1:])
    for i in signs:

        tmp1 = float(groups[0])
        tmp2 = float(groups[1])
        groups[0] = func[i](tmp1, tmp2)

        if SHOW_ACTIONS:
            global actions
            print(f'{actions}) {tmp1} {i} {tmp2} = {groups[0]}')
            actions += 1

        del groups[1]

    return groups[0]

def work(exp: str) -> str:
    while True:
        brackets: tuple = get_bracket(exp)
        if brackets:
            first_bracket = brackets[0]
            second_bracket = brackets[1]
            if not brackets[2][0] is None:
                func = brackets[2][0]
                func_last_ind = brackets[3]
                if not brackets[2][1] is None:
                    func_second_arg = brackets[2][1]
                else:
                    func_second_arg = None
                if func == 'sgm':
                    exp = exp[:first_bracket-len(func)] + \
                          str(exp[first_bracket+1:second_bracket], func, func_second_arg) + \
                          exp[func_last_ind + 1:]
                else:
                    exp = exp[:first_bracket-len(func)] + \
                          str(float(work(exp[first_bracket+1:second_bracket])), func, func_second_arg) + \
                          exp[func_last_ind + 1:]
            else:
                exp = exp[:first_bracket] + work(exp[first_bracket+1:second_bracket]) + exp[second_bracket+1:]
        else:
            break
    return processing_plus_minus(exp)