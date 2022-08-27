import pyautogui
import time
import pyperclip

weathers = ["서울 날씨", "광주 날씨", "성남 날씨", "제주 날씨", "부산 날씨"]

# while True:
#     print(pyautogui.position())
#     time.sleep(0.1)

addr_x = 1195
addr_y = 81
start_x = 1004
start_y = 303
end_x = 1890
end_y = 960

for w in weathers:
    pyautogui.moveTo(addr_x, addr_y)
    time.sleep(0.2)
    pyautogui.click()
    time.sleep(0.2)

    pyautogui.write("www.naver.com", interval=0.1)
    pyautogui.write(["enter"])
    time.sleep(1)

    pyperclip.copy(w)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.5)
    pyautogui.write(["enter"])
    time.sleep(1)
    save_path = "python_mini_projects\project2\\automouse\\" + w + '.png'
    pyautogui.screenshot(save_path, region=(
        start_x, start_y, end_x-start_x, end_y-start_y))
