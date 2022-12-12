from playwright.sync_api import Page
from typing import List


class DuckDuckGoResultPage:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.result_descriptions_containers = page.locator('.OgdwYG6KE2qthn9XQWFC span')
        self.seatch_input = page.locator('#search_form_input')

    def result_descriptions(self) -> List[str]:
        self.result_descriptions_containers.nth(8).wait_for()
        return self.result_descriptions_containers.all_text_contents()

    def result_descriptions_contains_phrase(self, validating_keywords: List[str], miniumum_results: int = 1) -> bool:
        descriptions = self.result_descriptions()
        # matches = [desc for desc in descriptions if phrase.lower() in desc.lower()]
        matches = [desc for desc in descriptions if any(val_key in desc.lower() for val_key in validating_keywords)]
        return len(matches) >= miniumum_results
