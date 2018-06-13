from collections import deque


def main():
    # считываем количество вершин и количество ребер
    (count_of_nodes, count_of_edges) = (int(x) for x in input().split(maxsplit=1))

    visited = {}

    # инициализируем матрицу смежности
    graph = [[0 for _ in range(count_of_nodes)] for _ in range(count_of_nodes)]

    # заполняем матрицу смежности
    for _ in range(count_of_edges):
        (node_1, node_2) = (int(x) - 1 for x in input().split(maxsplit=1))
        graph[node_1][node_2] += 1
        graph[node_2][node_1] += 1

    # проверяем степени вершин
    i = 0
    while i < count_of_nodes:
        k = sum(graph[i])
        if graph[i][i] > 0:
            k += graph[i][i]
        if k % 2:
            print('NONE')
            return
        i += 1

    # эйлеров цикл
    cycle = []

    # fake stack
    d = deque()
    d.append(1)
    while d:
        node = d[0] - 1

        # пометили вершину
        if visited.get(node) is None:
            visited[node] = True

        # посчитали степень
        k = sum(graph[node])

        # если есть петли
        if graph[node][node] > 0:
            k += graph[node][node]

        # ребер не найдено, добавляем в цикл, снимаем с вершины стэка
        if k == 0:
            cycle.append(node + 1)
            d.popleft()
        i = 0

        while i < count_of_nodes:
            if graph[node][i] == 0:
                i += 1
                continue

            # удаляем ребро
            graph[node][i] -= 1
            graph[i][node] -= 1

            # кладем в стек
            d.appendleft(i + 1)
            break

    # изначально я предварительно считал компоненты связности, но для этой задачи хватает такой проверки
    if len(visited) != count_of_nodes:
        print('NONE')
        return

    print(" ".join([str(x) for x in cycle[:-1]]))


if __name__ == '__main__':
    main()