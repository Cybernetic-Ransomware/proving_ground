from SixFeetUp.pages.search import DuckDuckGoSearchPage
from SixFeetUp.pages.result import DuckDuckGoResultPage
from playwright.sync_api import expect, Page


r"""
    to run with visible effects:
        py -m pytest SixFeetUp\tests --headed --slowmo 500

"""

searching_phrase = 'halfling badger rider'
validating_keywords = ['old world', 'warhammer', 'mootland', 'empire', 'ogre']


def test_basic_duckduckgo_search(page: Page) -> None:
    search_page = DuckDuckGoSearchPage(page)
    result_page = DuckDuckGoResultPage(page)

    search_page.load()
    search_page.search(searching_phrase)

    expect(result_page.seatch_input).to_have_value(searching_phrase)

    assert result_page.result_descriptions_contains_phrase(validating_keywords)

    expect(page).to_have_title('halfling badger rider at DuckDuckGo')

    pass
