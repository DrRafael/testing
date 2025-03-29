import string
from password.new_password import generate_password

def test_password_characters():
    """Тест, что при генерации используются только допустимые символы"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Генерируем длинный пароль для более надежной проверки
    for char in password:
        assert char in valid_characters

"""
Допиши еще один тест из предложенных. Или придумай свой.
Если сможешь написать больше, то будет круто!


Тест, что два сгенерированных подряд пароля различаются
"""
def test_password_length():
    password_length = 10
    password = generate_password(password_length)
    #Тест, что длина пароля соответствует заданной
    assert len(password) == 10

def test_password_two():
    password_length = 10
    password = generate_password(password_length)
    password1 = generate_password(password_length)
    #Тест, что длина пароля соответствует заданной
    assert password != password1