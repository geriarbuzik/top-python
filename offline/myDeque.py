from collections import deque

stack = deque()

stack.append(1)
stack.append(2)
stack.append(3)

print(stack.pop())
print(stack.pop())
print(stack.pop())

if not stack:
    print("Стек пуст")

"""
append(x)     добавляет элемент x в конец стека
pop()         удаляет и возвращает последний элемент стека
if not stack  проверка, пуст ли стек
clear()
stack[-1]     Peek Просмотр верхнего элемента
"""

"""
Дана строка, содержащая скобки различных типов: (), [], {}. 
Необходимо проверить, является ли скобочная последовательность корректной. 
Корректная последовательность означает, 
что каждой открывающей скобке соответствует закрывающая скобка того же типа, 
и скобки правильно вложены друг в друга.
"""

str1 = "()[]{}" # True
str2 = "([{}])" # True
str3 = "(]" # False
str4 = "([)]" # False

queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)

print(queue.popleft())
print(queue.popleft())
print(queue.popleft())

if not queue:
    print("Очередь пуста")

"""
реализовать class структуру данных очередь
добавление элемента в очередь enqueue
удаление элемента из очереди dequeue
получение максимального элемента в очереди get_max
получение минимального элемента в очереди get_min

использовать deque 
"""

