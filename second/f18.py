def swap(p_from, p_to):
    print(0, p_from, p_to)
    return


def move_single_element(n, p_from, p_to):
    # рекурсивно перемещает по 1 элементу на нужное место (на p_to)
    # (1 элемент лежит и над ним нет кучи, куча в 6 - p_from - p_to)
    if n <= 0:
        return
    if n == 1:
        print(1, p_from, p_to)
        return
    # достаем нижний из кучи
    put_from_bottom(n - 1, 6 - p_from - p_to, p_to)
    # перемещаем кучу (она подвинулась после 1 шага)
    hanoi(n - 3, p_from, 6 - p_from - p_to)
    # делаем свап
    swap(p_from, p_to)
    # теперь у нас лежит n-1 нужно рекурсивно подвинуть
    move_single_element(n - 1, p_from, p_to)


def hanoi(n, p_from, p_to):
    # перемещает кучу
    if n <= 0:
        return
    if n == 1:
        print(1, p_from, p_to)
        return
    # тащим нижний на нужное место
    put_from_bottom(n, p_from, p_to)
    # нужно подвинуть n-1 на нужное место, рекурсивно
    move_single_element(n - 1, p_from, p_to)


def put_from_bottom(n, p_from, p_to):
    # кладет нижний из кучи на нужное место. если переместить из 1 в 3, получится: n-1, башня n-2, n
    if n <= 0:
        return
    if n == 1:
        print(1, p_from, p_to)
        return
    if n == 2:
        put_from_bottom(n - 1, p_from, p_to)
        swap(p_from, p_to)
    if n == 3:
        put_from_bottom(n - 1, p_from, p_to)
        print(1, p_from, 6 - p_from - p_to)
        swap(p_from, p_to)
    if n >= 4:
        # сначала кладем n-1. получим что над n который хотим положить лежит n-2; n-3 куча лежит рядом; n-1 лежит там где надо
        put_from_bottom(n - 1, p_from, p_to)
        # двигаем башню -1(чтобы свапнуть с нижним элементом) которая выстроится на соседнем
        hanoi(n - 4, 6 - p_from - p_to, p_to)
        # свап с нижним, теперь над n лежит n-3
        swap(p_from, 6 - p_from - p_to)
        # теперь рекурсивно двигаем n-3 на другое место, чтобы освободить n
        move_single_element(n - 3, p_from, 6 - p_from - p_to)
        # наконец можем сделать swap
        swap(p_from, p_to)
