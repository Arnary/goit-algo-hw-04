# Опис роботи

Для порівняння алгоритмів сортування злиттям, вставкою, то вбудованих у Python функцій сортування sort та sorted, які використовують Timsort — гібридний алгоритм сортування, що поєднує в собі сортування злиттям і сортування вставками, за їхньою ефективністю було використано емпіричні дані тестування на наборах різного розміру.

Цей код генерує тестові дані розміром 1000, 10000 та 1000000 елементів і вимірює час виконання алгоритмів за допомогою модуля timeit. Тимчасові результати можуть значно змінюватися в залежності від конкретної реалізації алгоритмів та конфігурації обладнання.

## Висновки

Отримані результати тестування:

| Algorithm      | Processing time for small data | Processing time for medium data | Processing time for large data |
| -------------- | ------------------------------ | ------------------------------- | ------------------------------ |
| Insertion sort | 0.119935                       | 11.646399                       | 1342.431835                    |
| Merge sort     | 0.010775                       | 0.138511                        | 1.708073                       |
| Python sorted  | 0.000338                       | 0.007113                        | 0.101388                       |
| Python sort    | 0.000239                       | 0.007432                        | 0.098483                       |

Загальний висновок полягає в тому, що алгоритм Timsort, який комбінує сортування злиттям і вставками, демонструє велику ефективність на різних типах даних, особливо його перевага помітна на великому наборі даних. Злиття та вставки у Timsort дозволяють адаптуватися до властивостей конкретного набору даних, забезпечуючи оптимальний час виконання у більшості випадків. Таким чином, у реальних програмах важливо використовувати вбудовані функції сортування для забезпечення оптимальної продуктивності.
