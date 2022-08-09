from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

DRIVER_PATH = "/Selenium_Lesson_16/drivers/chromedriver.exe"

XPATHS_of_buttons = ["//button[contains(.,\'Оставить только гласные\')]",
                     "//button[contains(.,\'Ну и ещё пробелы\')]",
                     "//button[contains(.,\'Оставить ещё и .,-!?\')]",
                    ]

def test_horizontal_adaptive_layout():

    # Open the site in the selected resolution
    chrome_driver = webdriver.Chrome(DRIVER_PATH)
    chrome_driver.get("https://rioran.github.io/ru_vowels_filter/main.html")
    chrome_driver.set_window_size(1024, 800)
    sleep(1)

    # Search of last button position
    coordinates = chrome_driver.find_element(By.XPATH, "//button[contains(.,\'Выделить результат\')]")
    location = coordinates.location
    location.pop("x")
    last_y = location["y"]

    # Check the horizontal position of buttons
    coordination_of_buttons = True
    for paths in XPATHS_of_buttons[::-1]:
        coordinates = chrome_driver.find_element(By.XPATH, paths)
        location = coordinates.location
        location.pop("x")
        y_coordinate_of_button = location["y"]
        if y_coordinate_of_button != last_y:
            coordination_of_buttons = False

        assert coordination_of_buttons == True

    chrome_driver.quit()


def test_vertical_adaptive_layout():

    # Open the site in the selected resolution
    chrome_driver = webdriver.Chrome(DRIVER_PATH)
    chrome_driver.get("https://rioran.github.io/ru_vowels_filter/main.html")
    chrome_driver.set_window_size(200, 650)
    sleep(1)

    # Search of last button position
    coordinates = chrome_driver.find_element(By.XPATH, "//button[contains(.,\'Выделить результат\')]")
    location = coordinates.location
    location.pop("x")
    last_y = location["y"]

    # Check the vertical position of buttons
    coordination_of_buttons = True
    for paths in XPATHS_of_buttons[::-1]:
        coordinates = chrome_driver.find_element(By.XPATH, paths)
        location = coordinates.location
        location.pop("x")
        y_coordinate_of_button = location["y"]
        if y_coordinate_of_button > last_y:
            coordination_of_buttons = False
        else:
            last_y = y_coordinate_of_button

        assert coordination_of_buttons == True

    chrome_driver.quit()
