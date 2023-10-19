import pytest
import pyperclip
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from constants import XPATH_OF_BUTTONS
from constants import INPUT_TEXT
from constants import OUTPUT_TEXT


@pytest.mark.parametrize(
    "input_text, number_of_input_text",
    [(INPUT_TEXT[0], 0), (INPUT_TEXT[1], 1), (INPUT_TEXT[2], 2)],
)
def test_work_of_3_transforming_buttons_and_selection_one(
    input_text, number_of_input_text, chrome_driver
):

    # Open the site in the selected resolution
    chrome_driver.maximize_window()

    # Input the text
    chrome_driver.implicitly_wait(3)
    element_text_input = chrome_driver.find_element(By.ID, "text_input")
    element_text_input.clear()
    element_text_input.send_keys(input_text)

    # cycle of pushing buttons
    index_output_text = 0
    for paths in XPATH_OF_BUTTONS:
        chrome_driver.implicitly_wait(3)
        chrome_driver.find_element(By.XPATH, paths).click()
        output_text = chrome_driver.find_element("id", "text_output").text

        # comparing the right examples and the outputted texts from the site
        assert OUTPUT_TEXT[number_of_input_text][index_output_text] == output_text

        # checking the selection button
        chrome_driver.implicitly_wait(3)
        chrome_driver.find_element(
            By.XPATH, "//button[contains(.,'Выделить результат')]"
        ).click()
        act = ActionChains(chrome_driver)
        act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
        highlighted_text = str(pyperclip.paste())
        highlighted_text = highlighted_text.replace("\r", "")
        if output_text != "":
            assert highlighted_text == output_text

        index_output_text += 1

    chrome_driver.quit()
