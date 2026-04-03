from playwright.sync_api import Page, expect


class AddEmployeePage:
    def __init__(self, page: Page):
        self.page = page

        self.title = page.get_by_role("heading", name="Add Employee")

        self.first_name = page.get_by_placeholder("First Name")
        self.middle_name = page.get_by_placeholder("Middle Name")
        self.last_name = page.get_by_placeholder("Last Name")

        self.employee_id = page.locator("div.oxd-form-row input").nth(3)

        self.create_login_toggle = page.locator("span.oxd-switch-input")
        self.password_fields = page.locator('input[type="password"]')
        self.save_button = page.get_by_role("button", name="Save")

    def assert_loaded(self):
        expect(self.title).to_be_visible(timeout=15000)
        expect(self.first_name).to_be_visible(timeout=15000)

    def fill_name(self, first: str, middle: str, last: str):
        self.first_name.fill(first)
        self.middle_name.fill(middle)
        self.last_name.fill(last)

    def set_employee_id(self, emp_id: str):
        self.employee_id.fill(emp_id)
        expect(self.employee_id).to_have_value(emp_id)

    def enable_login_details(self):
        expect(self.create_login_toggle).to_be_visible(timeout=15000)
        self.create_login_toggle.click()
        expect(self.password_fields.first).to_be_visible(timeout=15000)

    def fill_login_details(self, username: str, password: str):
        username_input = self.page.locator("input.oxd-input.oxd-input--active").nth(5)

        username_input.fill(username)
        self.password_fields.nth(0).fill(password)
        self.password_fields.nth(1).fill(password)

        expect(username_input).to_have_value(username)
        expect(self.password_fields.nth(0)).to_have_value(password)
        expect(self.password_fields.nth(1)).to_have_value(password)

    def save(self):
        self.save_button.click()
