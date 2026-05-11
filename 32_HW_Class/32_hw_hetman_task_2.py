# Класс Counter

# Реализуйте класс Counter, который представляет собой простой счётчик.

# Счётчик должен начинаться с нуля.

# Предусмотрите методы для увеличения и уменьшения значения на единицу, 
# при этом при каждой операции должно отображаться новое значение счётчика.

# Добавьте метод, возвращающий текущий результат.

# Проверьте работу счётчика, выполнив несколько операций.
class Counter:
    CNT = 0
    
    def __init__(self):
        self.cnt = Counter.CNT

    def increase(self):
        self.cnt += 1
        return f"The value was increased, curren value is {self.cnt}"

    def decrease(self):
        self.cnt -= 1
        return f"The value was decreased, curren value is {self.cnt}"

    def get_cnt(self):
        return f"Current value of the counter: {self.cnt}"
    
counter_one = Counter()
print(counter_one.get_cnt())
print(counter_one.increase())
print(counter_one.increase())
print(counter_one.increase())
print(counter_one.increase())
print(counter_one.decrease())
print(counter_one.decrease())
print(counter_one.get_cnt())
