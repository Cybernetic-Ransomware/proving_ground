from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, slow_mo=50)
    page = browser.new_page()
    page.goto('https://www.thingiverse.com/search?type=things&q=&sort=popular&posted_after=now-30d')
    page.fill('input[class="SearchInput__searchInput--TvGY2"]', 'dungeon')
    page.press('input[class="SearchInput__searchInput--TvGY2"]', 'Enter')
    page.is_visible('a.ThingCardHeader__cardTitleLink--1xidi')

    searched_minis = page.inner_html('a.ThingCardHeader__cardTitleLink--1xidi')  # TODO: find a way to get all elements
    # searched_minis = page.inner_html('div.SearchResult__searchResultItems--2XMQB undefined')  # false search

    soup = BeautifulSoup(searched_minis, 'html.parser')

    print(soup.find_all('span'))
