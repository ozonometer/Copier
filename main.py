""""
https://pyautogui.readthedocs.io/en/latest/index.html
pyautogui.position() to get cursor position

"""""

import pyautogui
import time

numeral_map = tuple(zip(
    (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
    ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
))


def int_to_roman(i):
    result = []
    for integer, numeral in numeral_map:
        count = i // integer
        result.append(numeral * count)
        i -= integer * count
    return ''.join(result)


def roman_to_int(n):
    i = result = 0
    for integer, numeral in numeral_map:
        while n[i:i + len(numeral)] == numeral:
            result += integer
            i += len(numeral)
    return result


def save(index, roman):

    pyautogui.hotkey('shift', 'ctrl', 'q')
    pyautogui.moveTo(823, 1203, 1)  # location of snagit editor, can be replaces by pyautogui.screenshot()
    time.sleep(2.5)
    pyautogui.click()
    pyautogui.hotkey('ctrl', 's')
    time.sleep(1.0)
    if roman:
        pyautogui.typewrite(int_to_roman(index))
    else:
        pyautogui.typewrite(str(index))
    time.sleep(1.0)
    pyautogui.press('enter')
    print("page " + str(index) + " saved")
    pyautogui.moveTo(90, 180, 1)  # location of nex page button
    pyautogui.click()
    time.sleep(2.0)
    return


print("start")
for y in range(34):  # how many pages with roman numerals
    save(y, True)
for x in range(1, 3):  # how many pages with arab numbers
    save(x, False)
