def main():

    # считываем количество вершин и количество ребер
    (count_of_nodes, count_of_edges) = (int(x) for x in input().split(maxsplit=1))

    # инициализируем список смежности
    graph = {x+1: [] for x in range(count_of_nodes)}

    # "покраска" графа
    visited = {x+1: False for x in range(count_of_nodes)}

    # заполняем список смежности
    for _ in range(count_of_edges):
        (node_1, node_2) = (int(x) for x in input().split(maxsplit=1))
        graph[node_1].append(node_2)
        graph[node_2].append(node_1)

    # поиск в глубину
    def dfs(arr):
        for node in arr:
            if visited[node]:
                continue
            visited[node] = True
            for relates in graph[node]:
                if visited[relates]:
                    continue
                visited[relates] = True
                dfs(graph[relates])

    # компонента связности
    result = 0

    # обход каждой вершины
    for node, relates in graph.items():
        if visited[node]:
            continue
        visited[node] = True
        result +=1
        dfs(relates)

    print(result)


if __name__ == '__main__':
    main()