import pyautogui as au
import time


def multi_symbols():
    from_date = "01-01-"
    to_date = "31-12-"
    year = 2019
    chrome = au.click(x=914, y=1057)  # Chrome (zoom 110%)

    while year < 2022:
        chrome
        x = 0
        time.sleep(1)
        au.click(x=111, y=15)  # sheet tab (list of companies in a column) (1st tab)
        au.hotkey('ctrl', 'up', 'ctrl', 'up')  # move to upside of list
        au.click(x=360, y=16)  # https://www1.nseindia.com/products/content/equities/equities/eq_security.htm (2nd tab)
        au.click(x=1144, y=404)  # select series
        au.click(x=1139, y=634)  # EQ
        au.click(x=755, y=448)  # select a time period
        au.click(x=923, y=450)  # from date
        au.hotkey('ctrl', 'a', 'backspace')
        au.write(from_date + str(year))
        au.click(x=1040, y=449)  # to date
        au.hotkey('ctrl', 'a', 'backspace')
        au.write(to_date + str(year))

        while x < 240:
            au.click(x=111, y=15)  # sheet tab (1st tab)
            au.hotkey('down')  # go to next symbol
            au.hotkey('ctrl', 'c')  # copy symbol
            au.click(x=360, y=16)  # nse website (2nd tab)
            au.click(x=927, y=404)  # enter symbol
            au.hotkey('ctrl', 'a', 'backspace')
            au.hotkey('ctrl', 'v')  # paste symbol
            au.click(x=1195, y=451)  # get data button
            time.sleep(7)
            au.click(x=1367, y=515)  # download button
            x += 1

        chrome = None
        year += 1


def single_symbol():
    sym = "SBIN"
    c = au.click(x=124, y=1057)  # Chrome (zoom 100%)
    from_date = "01-01-"
    to_date = "30-09-"
    year = 2011
    x = 1
    while x:
        c
        au.click(x=360, y=16)  # nse website (2nd tab)
        au.click(x=927, y=384)  # enter symbol
        au.hotkey('ctrl', 'a', 'backspace')
        au.write(sym)
        au.click(x=1142, y=387)  # select series
        au.click(x=1117, y=598)  # EQ
        au.click(x=774, y=425)  # select a time period

        while year < 2015:
            au.click(x=927, y=428)  # from date
            au.hotkey('ctrl', 'a', 'backspace')
            au.write(from_date + str(year))
            au.click(x=1036, y=426)  # to date
            au.hotkey('ctrl', 'a', 'backspace')
            au.write(to_date + str(year))
            au.click(x=1168, y=428)  # get data button
            time.sleep(7)
            au.click(x=1343, y=488)  # download button
            year += 1

        x = None
