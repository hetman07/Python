# Комбинации одежды

# Напишите функцию, которая принимает списки типов одежды,
# цветов и размеров, а затем генерирует все возможные комбинации
# в формате "Clothe - Color - Size".
import itertools

clothes = ["T-shirt", "Jeans", "Jacket"]
colors = ["Red", "Blue", "Black"]
size = ["S", "M", "L"]

pairs = itertools.product(clothes, colors, size)

for cloth, col, siz in pairs:
    print(f"{cloth} - {col} - {siz}")

#2 variant
def generator_match_cloth(clothes, colors, sizes):
    for cloth in clothes:
        for color in colors:
            for size in sizes:
                yield f"{cloth}-{color}-{size}"
