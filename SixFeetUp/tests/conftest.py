import pytest

from SixFeetUp.pages.search import DuckDuckGoSearchPage
from SixFeetUp.pages.result import DuckDuckGoResultPage
from playwright.sync_api import Page


@pytest.fixture
def search_page(page: Page) -> DuckDuckGoSearchPage:
    return DuckDuckGoSearchPage(page)


@pytest.fixture
def result_page(page: Page) -> DuckDuckGoResultPage:
    return DuckDuckGoResultPage(page)


