import pyautogui
from time import sleep

# Posição de algo - use o mouseInfo
# Fazer algo com essa posição
pyautogui.moveTo(1368,461,duration=5)
for i in range(600):
    pyautogui.click()