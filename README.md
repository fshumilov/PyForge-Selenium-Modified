# PyForge-Selenium-Modified

This is the homework with following tasks for implementation:
1) Test all 4 buttons on this site (https://rioran.github.io/ru_vowels_filter/main.html)
2) Test with default, random and "zero" texts
3) Test the adaptive layout of the site. On the width screen the buttons should be presented horizontally, on the narrow screen - vertically

Additional:
1) Set it up as a local file for now and make sure all tests pass through PyTest
2) Submit your answers via the FORM (https://docs.google.com/forms/d/e/1FAIpQLSd2_hm2yVJu5pB1akQXjX_dUABFmMxaCR6SPYb3bpAAw89zcA/viewform) from your Quantori account - we will automatically identify you by mail.
3) A separate plus for those who apply any linter told by Dima to their code. I recommend pylint. Double plus - if this is a "we-make-python" build for flake8 (beware! may take hours!)
4) I am ready to check and comment on the works that will be handed in up to and including Wednesday.

How to start by terminal:
pytest

# UPDATES 
on 13.11.2022 according to the list of improvements (https://docs.google.com/document/d/10XHNBW49sfvLWeS3o4zsbdAZLv2VO6IqWxdYAbN0hbE/edit):
1) All constants are moved to the separate file "constanst.py"
2) The chrome_driver launches by a fixture. (The "scope='session'" was removed because it causes troubles with the "test_selenium_buttons_cycles_3_update.py" test)
3) The sleep function is substituted by the implicity_wait function
4) The "test_selenium_buttons_cycles_3_update.py" is decoupled by the @pytest.mark.parametrize into 3 tests
5) Some minor defects are fixed according to the list of improvements
