from playwright.sync_api import Page, expect


def test_verify_page_url(page: Page):
    page.goto("https://playwright.dev/python/docs/intro")
    page_url = page.url
    print("Page url is:", page_url)

    expect(page).to_have_url("https://playwright.dev/python/docs/intro")


def test_verifyTitle(page: Page):
    page.goto("https://playwright.dev/python/docs/intro")

    page_title = page.title()
    print("Title of page:", page_title)

    expect(page).to_have_title("Installation | Playwright Python")
