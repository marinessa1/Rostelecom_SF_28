valid_email = "aniram72006@yandex.ru"
valid_phone = "+79164618150"
valid_pass = "AS12345z"

invalid_email = 'nina2020@gmail.com'
invalid_pass = 'Das55555'

name = 'Марина'
surname = 'Алексеевна'
region = 'Москва г'
email = 'hcnhfnd@gmail.com'
password = 'ааа151515'

false_email = '123456'
false_mobile_max = '891674833888'
false_mobile_mini = '8916748338'
false_name_mini = 'А'
name_two_letters = "На"
thirty_letters = 'Приветприветприветприветпривет'
thirty_one_letters = 'Приветприветприветприветприветп'

class TestData:
    BASE_URL = 'https://b2c.passport.rt.ru/'

    #Заголовки названий элементов
    FORM_AUTH_MAIL = 'Почта'
    AUTH = 'Авторизация'
    RECOVERY = 'Восстановление пароля'
    CHECK = 'Регистрация'
    VERIFICATION_EMAIL = 'Подтверждение email'
    VERIFICATION_INVALID_EMAIL = 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'
    VERIFICATION_INVALID_NAME = 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
    ENTRY_VK = 'Войти'
    OK = 'Одноклассники'
    CHOICE_ACCOUNT = 'Вход'
    MM = 'Войти и разрешить'