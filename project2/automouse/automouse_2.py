# 서울날씨 검색, 화면 캡처 후 저장
import pyautogui
import time
import pyperclip
# while True:
#     print(pyautogui.position())
#     time.sleep(0.1)

pyautogui.moveTo(1335, 269, 0.2)
pyautogui.click()
time.sleep(0.5)

pyperclip.copy("서울 날씨")
pyautogui.hotkey("ctrl", "v")
time.sleep(0.5)

pyautogui.write(["enter"])
time.sleep(1)

start_x = 1004
start_y = 303

end_x = 1890
end_y = 960

pyautogui.screenshot(r'python_mini_projects\project2\서울날시.png', region=(
    start_x, start_y, end_x - start_x, end_y - start_y))
