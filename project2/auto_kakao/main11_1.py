import time
import pyautogui
import pyperclip
picPosition = pyautogui.locateOnScreen(
    r'python_mini_projects\\project2\\auto_kakao\\kakao_my1.PNG')
print(picPosition)


if picPosition is None:
    picPosition = pyautogui.locateOnScreen(
        r'python_mini_projects\\project2\\auto_kakao\\kakao_my1.PNG')
    print(picPosition)

if picPosition is None:
    picPosition = pyautogui.locateOnScreen(
        r'python_mini_projects\\project2\\auto_kakao\\kakao_my1.PNG')
    print(picPosition)
clickPosition = pyautogui.center(picPosition)
pyautogui.doubleClick(clickPosition)

pyperclip.copy("이 메세지는 자동으로 보낸 메세지입니다.")
pyautogui.hotkey("ctrl", "v")
time.sleep(1)

pyautogui.write(["enter"])
time.sleep(1)

pyautogui.write(["escape"])
time.sleep(1)
