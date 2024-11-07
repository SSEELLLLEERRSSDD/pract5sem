from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

def test_empty_login(page: Page) -> None:
    lp = LoginPage(page)
    lp.navigate()
    lp.login("standard_user", "")
    expect(lp.error).to_contain_text("Epic sadface: Password is required")