import re
import time

from playwright.sync_api import expect

from pages.add_employee_page import AddEmployeePage
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from pages.pim_page import PIMPage


def test_add_employee_with_login_details(page):
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
    add_emp.fill_name("Ahmad", "QA", "Automation")
    add_emp.set_employee_id(unique)

    add_emp.enable_login_details()
    add_emp.fill_login_details(f"ahmad_{unique}", "Admin123!")

    add_emp.save()

    expect(page.get_by_role("heading", name="Personal Details")).to_be_visible(timeout=20000)
    expect(page).to_have_url(re.compile(r".*/pim/viewPersonalDetails/empNumber/\d+$"))
