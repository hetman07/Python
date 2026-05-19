# Счётчик экземпляров

# Создайте класс User, представляющий пользователя.
# При создании должны указываться логин (username) и пароль (password).
# У класса должно быть поле total_users,
# хранящее общее количество созданных пользователей.
# При каждом создании нового объекта User, 
# счётчик должен увеличиваться.
# Добавьте метод get_total(), возвращающий количество пользователей.
# Проверьте, что счётчик работает.
class User:
    total_users = 0

    def __init__(self, username, password):
        self.username = username
        self.password = password
        
        User.increment_users()
    
    @classmethod
    def increment_users(cls):
        cls.total_users += 1

    @classmethod
    def get_total(cls):
        return f"Total users: {cls.total_users}"


user1 = User("Vita", "qwer12")
user2 = User("Vita", "qwer12")
user3 = User("Vita", "qwer12")

print(User.get_total())
