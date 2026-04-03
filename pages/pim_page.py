from playwright.sync_api import Page, expect


class PIMPage:
    def __init__(self, page: Page):
        self.page = page
        self.pim_title = page.get_by_role("heading", name="PIM")
        self.add_employee_tab = page.get_by_role("link", name="Add Employee")
        self.employee_list_tab = page.get_by_role("link", name="Employee List")

    def assert_pim_loaded(self):
        expect(self.pim_title).to_be_visible()

    def open_add_employee(self):
        self.add_employee_tab.click()

    def open_employee_list(self):
        self.employee_list_tab.click()
