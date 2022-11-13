from selenium.webdriver.common.by import By

from constants import XPATH_OF_BUTTONS_FROM_RIGHT_TO_LEFT


def test_horizontal_adaptive_layout(chrome_driver):

    # Open the site in the selected resolution
    chrome_driver.set_window_size(1024, 800)
    chrome_driver.implicitly_wait(3)

    # Search of last button position
    coordinates = chrome_driver.find_element(By.XPATH, "//button[contains(.,\'Выделить результат\')]")
    location = coordinates.location
    location.pop("x")
    last_y = location["y"]

    # Check the horizontal position of buttons
    for paths in XPATH_OF_BUTTONS_FROM_RIGHT_TO_LEFT:
        coordinates = chrome_driver.find_element(By.XPATH, paths)
        location = coordinates.location
        location.pop("x")
        y_coordinate_of_button = location["y"]

        assert y_coordinate_of_button == last_y


def test_vertical_adaptive_layout(chrome_driver):

    # Open the site in the selected resolution
    chrome_driver.set_window_size(200, 650)
    chrome_driver.implicitly_wait(3)

    # Search of last button position
    coordinates = chrome_driver.find_element(By.XPATH, "//button[contains(.,\'Выделить результат\')]")
    location = coordinates.location
    location.pop("x")
    last_y = location["y"]

    # Check the vertical position of buttons
    coordination_of_buttons = True
    for paths in XPATH_OF_BUTTONS_FROM_RIGHT_TO_LEFT:
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
