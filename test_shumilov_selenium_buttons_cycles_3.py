from time import sleep

from selenium import webdriver
import pyperclip
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

DRIVER_PATH = "C:\\Users\\filipp.shumilov\\PycharmProjects\\PyForgeQA\\Selenium_Lesson_16\\drivers\\chromedriver.exe"

INPUT_TEXT = [("Сменялись в детстве радугой дожди,\n"
               "Сияньем солнца — сумрачные тени.\n"
               "Но в зрелости не требуй и не жди\n"
               "Таких простых и скорых утешений.\n\n"
               "Самуил Яковлевич Маршак"),
              "рандом: оююВФЫВфбь лоюя,ю сфыббо!вф одфыыа,, ,одл;ы",
              "                                                   ",
              ]
OUTPUT_TEXT1 = [("еяиееауоои\n"
                 "ияеоауаыееи\n"
                 "оеоиееуиеи\n"
                 "аиоыиоыуееи\n\n"
                 "ауияоеиаа"),
                ("еяи ее ауо ои\n"
                 "ияе оа уаые еи\n"
                 "о еои е еу и е и\n"
                 "аи оы и оы уееи\n\n"
                 "ауи яоеи аа"),
                ("еяи ее ауо ои,\n"
                 "ияе оа уаые еи.\n"
                 "о еои е еу и е и\n"
                 "аи оы и оы уееи.\n\n"
                 "ауи яоеи аа"),
                ]
OUTPUT_TEXT2 = ["аооююыоюяюыооыыаоы",
                "ао оююы оюяю ыо оыыа оы",
                "ао оююы оюя,ю ыо! оыыа,, ,оы",
                ]
OUTPUT_TEXT3 = ["",
                "",
                "",
                ]
OUTPUT_TEXT = [OUTPUT_TEXT1, OUTPUT_TEXT2, OUTPUT_TEXT3]

XPATHS_of_buttons = ["//button[contains(.,\'Оставить только гласные\')]",
                     "//button[contains(.,\'Ну и ещё пробелы\')]",
                     "//button[contains(.,\'Оставить ещё и .,-!?\')]",
                     ]

chrome_driver = webdriver.Chrome(DRIVER_PATH)
chrome_driver.get("https://rioran.github.io/ru_vowels_filter/main.html")
chrome_driver.maximize_window()


def test_work_of_3_transforming_buttons_and_selection_one():
    # cycle of inputted texts
    number_of_input_text = 0
    for variant_text in INPUT_TEXT:
        sleep(0.1)
        chrome_driver.find_element(By.ID, "text_input").clear()
        chrome_driver.find_element(By.ID, "text_input").send_keys(variant_text)

        # cycle of pushing buttons
        index_output_text = 0
        for paths in XPATHS_of_buttons:
            sleep(0.1)
            chrome_driver.find_element(By.XPATH, paths).click()
            output_text = chrome_driver.find_element("id", "text_output").text

            # comparing the right examples and the outputted texts from the site
            assert OUTPUT_TEXT[number_of_input_text][index_output_text] == output_text

            # checking the selection button
            sleep(0.1)
            chrome_driver.find_element(By.XPATH, "//button[contains(.,\'Выделить результат\')]").click()
            act = ActionChains(chrome_driver)
            act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
            highlighted_text = str(pyperclip.paste())
            highlighted_text = highlighted_text.replace("\r", "")
            if output_text != "":
                assert highlighted_text == output_text

            index_output_text += 1

        number_of_input_text += 1

    chrome_driver.quit()
