from pages.dashboard_page import DashboardPage
from pages.employee_list_page import EmployeeListPage
from pages.login_page import LoginPage
from pages.pim_page import PIMPage

VALID_FIRST_NAME = "mohammad"
VALID_LAST_NAME = "hanani"
VALID_EMPLOYEE_ID = "0394"


def login_and_open_employee_list(page):
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)
    pim_page = PIMPage(page)

    login_page.open()
    login_page.login("Admin", "admin123")

    dashboard_page.assert_dashboard_loaded()
    dashboard_page.go_to_pim()

    pim_page.assert_pim_loaded()
    pim_page.open_employee_list()


def test_search_employee_by_valid_name(page):
    login_and_open_employee_list(page)

    employee_list_page = EmployeeListPage(page)
    employee_list_page.assert_loaded()

    employee_list_page.search_by_valid_name(VALID_FIRST_NAME)
    employee_list_page.assert_employee_name_in_results(VALID_FIRST_NAME)


def test_search_employee_by_valid_id(page):
    login_and_open_employee_list(page)

    employee_list_page = EmployeeListPage(page)
    employee_list_page.assert_loaded()

    employee_list_page.search_by_id(VALID_EMPLOYEE_ID)
    employee_list_page.assert_employee_id_in_results(VALID_EMPLOYEE_ID)


def test_search_employee_by_invalid_name(page):
    login_and_open_employee_list(page)

    employee_list_page = EmployeeListPage(page)
    employee_list_page.assert_loaded()

    employee_list_page.search_by_invalid_name("NoSuchEmployeeXYZ")
    employee_list_page.assert_no_records_found()


def test_search_employee_by_invalid_id(page):
    login_and_open_employee_list(page)

    employee_list_page = EmployeeListPage(page)
    employee_list_page.assert_loaded()

    employee_list_page.search_by_id("999999")
    employee_list_page.assert_no_records_found()
