from playwright.sync_api import expect, Page


"""
    to run with visible effects:
        py -m pytest tests --headed --slowmo 1000  

"""

searching_phrase = 'halfling badger rider'
validating_keywords = ['old world', 'warhammer', 'mootland', 'empire', 'ogre']


def test_basic_duckduckgo_search(page: Page) -> None:
    page.goto('https://duckduckgo.com')

    page.locator('id=search_form_input_homepage').fill(searching_phrase)
    page.locator('id=search_button_homepage').click()

    #   same as above
    # page.locator('xpath=//*[@id="search_form_input_homepage"]').fill('halfling badger rider')
    # page.locator('xpath=//*[@id="search_button_homepage"]').click()

    #   same but not recommended by documentation
    # page.fill('id=search_form_input_homepage', 'halfling badger rider')
    # page.locator('id=search_button_homepage').click()

    #   playwright builded in assertion
    expect(page.locator('id=search_form_input')).to_have_value(searching_phrase)

    #   pytest way, but without a waiting till appear
    # assert 'halfling badger rider' == page.input_value('id=search_form_input')

    # class ="OgdwYG6KE2qthn9XQWFC"
    page.locator('.OgdwYG6KE2qthn9XQWFC span').nth(8).wait_for()
    descriptions = page.locator('.OgdwYG6KE2qthn9XQWFC span').all_text_contents()

    #  filter descriptions to ones including the keyword/s list, left mindflow for reminder
    # matches = [desc for desc in descriptions if validating_keywords[0] in desc.lower()]
    # matches = [desc for desc in descriptions for val_keyword in validating_keywords if val_keyword in desc.lower()]
    matches = [desc for desc in descriptions if any(val_key in desc.lower() for val_key in validating_keywords)]

    assert len(matches) > 0

    pass
