import re
import time

from playwright.sync_api import expect

from pages.add_employee_page import AddEmployeePage
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from pages.pim_page import PIMPage


def test_add_employee_basic(page):
    # Login
    login = LoginPage(page)
    login.open()
    login.login("Admin", "admin123")

    # Dashboard
    dashboard = DashboardPage(page)
    dashboard.assert_dashboard_loaded()
    dashboard.go_to_pim()

    # PIM Page
    pim = PIMPage(page)
    pim.assert_pim_loaded()
    pim.open_add_employee()

    # Add Employee Page
    add_emp = AddEmployeePage(page)
    add_emp.assert_loaded()

    # Create unique employee id
    unique = str(int(time.time()))

    # Fill employee data
    add_emp.fill_name("Ahmad", "Nahi", "Hanani")
    add_emp.set_employee_id(unique)

    # Save
    add_emp.save()

    # Verify success toast
    toast = page.locator(".oxd-toast")
    expect(toast).to_be_visible(timeout=20000)
    expect(toast).to_contain_text("Success")

    # Verify redirect to Personal Details page
    expect(page).to_have_url(re.compile(r".*/viewPersonalDetails.*"), timeout=30000)
    expect(page.get_by_role("heading", name="Personal Details")).to_be_visible()
