# Класс Rectangle

# Создайте класс Rectangle, который описывает прямоугольник.

# У каждого объекта должны быть два поля: width и height.

# Добавьте метод get_area(), который возвращает площадь прямоугольника.

# Создайте объект прямоугольника с произвольными значениями.

# Выведите его площадь.

# Измените ширину и высоту.

# Выведите новую площадь.
class Rectangle:
    def __init__(self, width, height):
        self.set_measure(width, height)
        
    def set_measure(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("The measure is belove than NULL.")
        self.width = width
        self.height = height
        
    def get_measure(self):
        return f"Width: {self.width}, Height: {self.height}."
    
    def get_area(self):
        return self.height*self.width
    
first_rectangl = Rectangle(5, 6)
print(first_rectangl.get_area())
print(first_rectangl.get_measure())
first_rectangl.set_measure(1,2)    
print(first_rectangl.get_measure())
print(first_rectangl.get_area())
