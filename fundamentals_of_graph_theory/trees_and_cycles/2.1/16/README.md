### Шаг 16

Задача
> На вход программе подаётся описание простого связного графа. Первая строка содержит два числа: число вершин V≤10000 и число рёбер E≤30000 графа. Следующие E строк содержат номера пар вершин, соединенных рёбрами. Вершины имеют номера от 0 до V−1. Выведите список из V чисел — расстояний от вершины 0 до соответствующих вершин графа.

Формат входных данных:
> На вход подаётся описание графа. В первой строке указаны два натуральных числа, разделенные пробелом: число вершин v≤10000 и число рёбер e≤30000. В следующих e строках содержатся описания рёбер. Каждое ребро задаётся разделённой пробелом парой номеров вершин, которые это ребро соединяет. Считается, что вершины графа пронумерованы числами от 1 до v.

Формат выходных данных:
> Список чисел - расстояние от вершины 0

### Пример работы программы

Sample Input 1:
> 6 7
> 0 1
> 1 2
> 2 0
> 3 2
> 4 3
> 4 2
> 5 4

Sample Output 1:
> 0 1 1 2 2 3