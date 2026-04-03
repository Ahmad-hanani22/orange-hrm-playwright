import os

import allure
import pytest


@pytest.fixture(scope="session", autouse=True)
def _create_allure_dir():
    os.makedirs("test-results", exist_ok=True)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            screenshot = page.screenshot()
            allure.attach(
                screenshot,
                name="failure-screenshot",
                attachment_type=allure.attachment_type.PNG,
            )
            allure.attach(
                page.url,
                name="failure-url",
                attachment_type=allure.attachment_type.TEXT,
            )
