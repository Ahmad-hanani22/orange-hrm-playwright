import re
import time
from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.pim_page import PIMPage
from pages.add_employee_page import AddEmployeePage


def test_add_employee_basic(page):
    login = LoginPage(page)
    login.open()
    login.login("Admin", "admin123")

    dashboard = DashboardPage(page)
    dashboard.assert_dashboard_loaded()
    dashboard.go_to_pim()

    pim = PIMPage(page)
    pim.assert_pim_loaded()
    pim.open_add_employee()

    add_emp = AddEmployeePage(page)
    add_emp.assert_loaded()

    unique = str(int(time.time()))
    add_emp.fill_name("Ahmad", "Nahi", "Hanani")
    add_emp.set_employee_id(unique)

    add_emp.save()

    toast = page.locator(".oxd-toast")
    expect(toast).to_be_visible(timeout=20000)
    expect(toast).to_contain_text("Success")

    expect(page).to_have_url(re.compile(r".*/viewPersonalDetails.*"), timeout=30000)
    expect(page.get_by_role("heading", name="Personal Details")).to_be_visible(timeout=30000)