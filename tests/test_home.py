from home_8_10 import RegistrationPage
from home_8_10 import User
import allure

registration_page = RegistrationPage()


def test_student_registration_form():
    with allure.step("Открыть страницу регистрации пользователей"):
        registration_page.open()
    with allure.step("Заполнить форму регистрации тестовыми данными"):
        student = User(first_name='Anton',
                   last_name='Fomin',
                   email='catman@mail.ru',
                   gender='Other',
                   phone_number='9694840725',
                   day_birth='019',
                   month_birth='3',
                   year_birth='90',
                   subject='Computer Science',
                   hobby='Sports, Reading',
                   picture='sun.jpg',
                   current_address='Krasnodar',
                   state='NCR',
                   city='Delhi')
    registration_page.open()

    # WHEN
    registration_page.register(student)
    with allure.step("Проверка, что пользователь зарегистрирован"):
        registration_page.student_should_by_registred(student)