from playwright.sync_api import Page


class DuckDuckGoSearchPage:

    URL = 'https://duckduckgo.com'

    def __init__(self, page: Page) -> None:
        self.page = page
        self.search_button = page.locator('id=search_button_homepage')
        self.seatch_input = page.locator('id=search_form_input_homepage')

    def load(self) -> None:
        self.page.goto(self.URL)

    def search(self, phrase: str) -> None:
        self.seatch_input.fill(phrase)
        self.search_button.click()
