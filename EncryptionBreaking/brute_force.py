from itertools import product
import pyautogui

pyautogui.MINIMUM_DURATION = 0
pyautogui.MINIMUM_SLEEP = 0
pyautogui.PAUSE = 0


def check_combos(length):
    combinations = product("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", repeat=length)
    while True:
        try:
            password = ''.join(next(combinations))
            pyautogui.typewrite(password)
            pyautogui.press('enter')
            pyautogui.press('enter')
        except StopIteration:
            break


check_combos(3)
