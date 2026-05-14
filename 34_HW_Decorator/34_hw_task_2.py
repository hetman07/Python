# Проверка данных пользователя

# Доработайте класс User.

# Добавьте валидации полей при создании.

# Имя должно быть непустой строкой.

# Пароль должен быть строкой длиной не менее 5 символов.

# Если данные некорректны — выбрасывайте ValueError.

# Добавьте строковое представление объекта.

# Проверьте работу класса с разными значениями.
class User:
    total_users = 0

    def __init__(self, username, password):
        self.is_valid_username(username)
        self.is_valid_password(password)

        self.username = username
        self.password = password

        User.total_users += 1

    @classmethod
    def get_total(cls):
        return f"Total users: {cls.total_users}"

    @staticmethod
    def is_valid_username(username):
        if not isinstance(username, str) or not username.strip():
            raise ValueError("Username is empty.")

    @staticmethod
    def is_valid_password(password):
        if len(password) < 5:
            raise ValueError("The password should be longer than 5 symbols.")

    def __str__(self):
        return f"User: {self.username}, {self.password}"


user1 = User("Vita", "qwer12")
print(user1)
user2 = User("Alina", "qwer12")
print(user2)
print(User.get_total())
# user3 = User("      ", "qwer12")
# print(user3)
user4 = User("Olha", "qwe")
print(user4)
print(User.get_total())
