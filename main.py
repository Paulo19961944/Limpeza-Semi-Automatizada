import time
import pyautogui

# Passo 1 -> Recent

pyautogui.hotkey('win', 'r')
time.sleep(3)
pyautogui.press('backspace')
pyautogui.write('recent')
pyautogui.press('enter')
time.sleep(5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'a', 'up')
pyautogui.press('del')
pyautogui.hotkey('ctrl', 'w')
pyautogui.hotkey('ctrl', 'w', 'up')


# Passo 2 -> Prefetch


pyautogui.hotkey('win', 'r')
time.sleep(3)
pyautogui.press('backspace')
pyautogui.write('prefetch')
pyautogui.press('enter')
time.sleep(10)
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'a', 'up')
pyautogui.press('del')
time.sleep(10)

pyautogui.keyDown('up')
pyautogui.press('enter')
time.sleep(2)
pyautogui.press('down')
time.sleep(2)
pyautogui.press('right')
time.sleep(2)
pyautogui.press('enter')
time.sleep(2)
pyautogui.hotkey('ctrl', 'w')
time.sleep(1)
pyautogui.hotkey('ctrl', 'w', 'up')
time.sleep(1)

# Passo 3 -> Temp


pyautogui.hotkey('win', 'r')
time.sleep(3)
pyautogui.press('backspace')
pyautogui.write('%temp%')
pyautogui.press('enter')
time.sleep(10)
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'a', 'up')
pyautogui.press('del')
time.sleep(10)

pyautogui.keyDown('up')
pyautogui.press('enter')
time.sleep(2)
pyautogui.press('down')
time.sleep(2)
pyautogui.press('right')
time.sleep(2)
pyautogui.press('enter')
pyautogui.hotkey('ctrl', 'w')
time.sleep(3)
pyautogui.hotkey('ctrl', 'w', 'up')
time.sleep(2)


# Passo 4 -> Cleanmgr

pyautogui.hotkey('win', 'r')
time.sleep(3)
pyautogui.press('backspace')
pyautogui.write('cleanmgr')
pyautogui.press('enter')
time.sleep(40)
pyautogui.press('enter')
time.sleep(2)
pyautogui.press('enter')
time.sleep(20)
