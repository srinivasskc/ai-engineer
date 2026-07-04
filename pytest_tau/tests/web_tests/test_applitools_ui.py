# url - https://demo.applitools.com/
# credentials are dummy.

import pytest
import re

from playwright.sync_api import Page, expect


@pytest.mark.ui
@pytest.mark.acmebank
def test_acme_bank_login(page: Page):
    # Arrange
    page.goto("https://demo.applitools.com/")

    # ACT
    page.locator("#username").fill("Srinivas")
    page.locator("#password").fill("Srinivas")
    page.locator("#log-in").click()

    # Assert - Web First Assertion (expect) instead of (assert)
    expect(page.locator("div.logo-w.menu-size")).to_be_visible()
    expect(page.locator("ul.main-menu")).to_be_visible()
    expect(page.get_by_text("Add Account")).to_be_visible()
    expect(page.get_by_text("Make Payment")).to_be_visible()
