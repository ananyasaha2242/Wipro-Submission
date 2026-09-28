import pytest
from selenium import webdriver
from selenium.common.exceptions import InvalidSessionIdException
from utils.read_properties import ReadConfig
import os


@pytest.fixture()
def setup(request):
    browser = ReadConfig.get_browser()

    if browser.lower() == 'chrome':
        driver = webdriver.Chrome()
    elif browser.lower() == 'firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()

    driver.implicitly_wait(10)
    driver.maximize_window()

    request.cls.driver = driver

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    pytest_html = item.config.pluginmanager.getplugin('html')

    outcome = yield
    report = outcome.get_result()

    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == 'setup':

        xfail = hasattr(report, 'wasxfail')

        if (report.skipped and xfail) or (report.failed and not xfail):

            file_name = (
                report.nodeid
                .replace("::", "_")
                .replace("/", "_")
                .replace(".py", "")
                + ".png"
            )

            file_name = "".join(
                [
                    c for c in file_name
                    if c.isalpha() or c.isdigit() or c in ['_', '.', '-']
                ]
            ).rstrip()

            screenshots_dir = os.path.join(
                os.path.dirname(__file__),
                '..',
                'Screenshots'
            )

            os.makedirs(screenshots_dir, exist_ok=True)

            file_path = os.path.join(
                screenshots_dir,
                file_name
            )

            driver = item.funcargs.get("setup", None)

            if driver is not None:

                try:
                    if driver.session_id is not None:

                        driver.save_screenshot(file_path)

                        html = (
                            f'<div>'
                            f'<img src="../Screenshots/{file_name}" '
                            f'alt="screenshot" '
                            f'style="width:304px;height:228px;" '
                            f'onclick="window.open(this.src)" '
                            f'align="right"/>'
                            f'</div>'
                        )

                        extra.append(
                            pytest_html.extras.html(html)
                        )

                except InvalidSessionIdException:
                    pass

        report.extra = extra