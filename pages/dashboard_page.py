from playwright.sync_api import Page, expect


class DashboardPage:
    def __init__(self, page: Page):
        self.page: Page = page
        self.dashboard_header = page.get_by_role("heading", name="Dashboard")
        self.pim_menu = page.get_by_role("link", name="PIM")

    def assert_dashboard_loaded(self):
        expect(self.dashboard_header).to_be_visible()

    def go_to_pim(self):
        self.pim_menu.click()
