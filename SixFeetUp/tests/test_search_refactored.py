from SixFeetUp.pages.search import DuckDuckGoSearchPage
from SixFeetUp.pages.result import DuckDuckGoResultPage
from playwright.sync_api import expect, Page


r"""
    to run with visible effects:
        py -m pytest SixFeetUp\tests --headed --slowmo 500
        
    to run on otcher browser engines, e.g. Firefox:
        py -m pytest SixFeetUp\tests --headed --slowmo 500 --browser firefox       
         
    to run multiple on different browser engines:
        py -m pytest SixFeetUp\tests --browser firefox --browser chromium --browser webkit -v
        
    to run directly on a browser (chrome vs chromium)
        py -m pytest SixFeetUp\tests --browser-channel chrome
        
    to test on an emulation of a mobile device
        py -m pytest SixFeetUp\tests --headed --slowmo 500 --device "iPad Mini"
        list of emulable devices: 
           https://github.com/microsoft/playwright/blob/main/packages/playwright-core/src/server/deviceDescriptorsSource.json  

"""

searching_phrase = 'halfling badger rider'
validating_keywords = ['old world', 'warhammer', 'mootland', 'empire', 'ogre']


def test_basic_duckduckgo_search(
        page: Page,
        search_page: DuckDuckGoSearchPage,
        result_page: DuckDuckGoResultPage) -> None:

    search_page.load()
    search_page.search(searching_phrase)

    expect(result_page.seatch_input).to_have_value(searching_phrase)

    assert result_page.result_descriptions_contains_phrase(validating_keywords)

    expect(page).to_have_title('halfling badger rider at DuckDuckGo')

    pass
