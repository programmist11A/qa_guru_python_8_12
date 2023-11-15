from selene import browser, be, have
from home_8_10.picture.resource import path

class RegistrationPage:
    def open(self):
        browser.open('/automation-practice-form')
        browser.execute_script('document.querySelector("#fixedban").remove()')
        browser.element('footer').execute_script('element.remove()')

    def register(self, user):
        browser.element('#firstName').should(be.visible).type(user.first_name)
        browser.element('#lastName').should(be.visible).type(user.last_name)
        browser.element('#userEmail').should(be.visible).type(user.email)
        browser.all('.custom-radio').element_by(have.text(user.gender)).click()
        browser.element('#userNumber').should(be.visible).type(user.phone_number)
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').should(be.visible).click()
        browser.element(f'.react-datepicker__month-select > option:nth-child({user.month_birth})').should(be.visible).click()
        browser.element('.react-datepicker__year-select').should(be.visible).click()
        browser.element(f'.react-datepicker__year-select > option:nth-child({user.year_birth})').should(be.visible).click()
        browser.element(f'.react-datepicker__day.react-datepicker__day--{user.day_birth}').should(be.visible).click()
        browser.element('#subjectsInput').should(be.visible).type(user.subject).press_enter()
        if 'Sports' in user.hobby:
            browser.element('label[for=hobbies-checkbox-1]').should(be.visible).click()
        if 'Reading' in user.hobby:
            browser.element('label[for=hobbies-checkbox-2]').should(be.visible).click()
        browser.element('#uploadPicture').set_value(path(user.picture))
        browser.element('#currentAddress').should(be.visible).type(user.current_address)
        browser.element("#react-select-3-input").should(be.visible).type(user.state).press_enter()
        browser.element("#react-select-4-input").should(be.visible).type(user.city).press_enter()
        browser.element("#submit").press_enter()

    def student_should_by_registred(self, user):
        browser.all(".table-dark>tbody>tr>td:nth-child(2)").should(have.texts(
            f'{user.first_name} {user.last_name}',
            user.email,
            user.gender,
            user.phone_number,
            f"{user.day_birth.replace('0', '')} "
            f"{user.month_birth.replace('3', 'March')},"
            f"{user.year_birth.replace('90', '1989')}",
            user.subject,
            user.hobby,
            user.picture,
            user.current_address,
            f'{user.state} {user.city}'
        ))