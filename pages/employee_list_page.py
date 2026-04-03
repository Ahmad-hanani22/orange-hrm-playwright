from playwright.sync_api import Page, expect


class EmployeeListPage:
    def __init__(self, page: Page):
        self.page = page

        self.title = page.get_by_role("heading", name="PIM")
        self.employee_name_input = page.get_by_placeholder("Type for hints...").first

        self.employee_id_input = page.locator("div.oxd-form-row input").nth(1)

        self.search_button = page.get_by_role("button", name="Search")
        self.reset_button = page.get_by_role("button", name="Reset")

        self.table_body = page.locator("div.oxd-table-body")
        self.no_records_message = page.locator("span.oxd-text").filter(has_text="No Records Found")

    def assert_loaded(self):
        expect(self.title).to_be_visible()
        expect(self.search_button).to_be_visible()

    def fill_employee_name(self, employee_name: str):
        self.employee_name_input.fill(employee_name)

    def fill_employee_id(self, employee_id: str):
        self.employee_id_input.fill(employee_id)

    def click_search(self):
        self.search_button.click()

    def click_reset(self):
        self.reset_button.click()

    def search_by_valid_name(self, employee_name: str):
        self.fill_employee_name(employee_name)

        option = self.page.locator("div[role='listbox'] span").filter(has_text=employee_name)
        option.first.wait_for(timeout=10000)
        option.first.click()

        self.click_search()
        self.page.wait_for_timeout(2000)

    def search_by_invalid_name(self, employee_name: str):
        self.fill_employee_name(employee_name)
        self.click_search()
        self.page.wait_for_timeout(2000)

    def search_by_id(self, employee_id: str):
        self.fill_employee_id(employee_id)
        self.click_search()
        self.page.wait_for_timeout(2000)

    def assert_no_records_found(self):
        expect(self.no_records_message).to_be_visible(timeout=10000)

    def assert_employee_name_in_results(self, employee_name: str):
        expect(self.table_body).to_contain_text(employee_name)

    def assert_employee_id_in_results(self, employee_id: str):
        expect(self.table_body).to_contain_text(employee_id)
