from collections import deque


def main():

    root = 0

    # считываем количество вершин и количество ребер
    (count_of_nodes, count_of_edges) = (int(x) for x in input().split(maxsplit=1))

    # инициализируем список смежности
    graph = {x: [] for x in range(count_of_nodes)}

    # "покраска" графа
    visited = {root: 0}

    # заполняем список смежности
    for _ in range(count_of_edges):
        (node_1, node_2) = (int(x) for x in input().split(maxsplit=1))
        graph[node_1].append(node_2)
        graph[node_2].append(node_1)

    # инициализируем очередь
    q = deque()
    q.append(root)

    while q:

        # берем вершину из очереди слева
        node = q.popleft()

        # обходим очередь в ширину
        for n in graph[node]:

            # если не вершина не помечена, помечаем ее "расстоянием" и добавляем в очередь справа
            if visited.get(n) is None:
                visited[n] = visited[node] + 1
                q.append(n)

    # выводим ответ
    print(" ".join([str(x[1]) for x in sorted(visited.items(), key=lambda x: x[0])]))


if __name__ == '__main__':
    main()