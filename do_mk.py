import time
import keyboard
import pyautogui

so_bat_dau = 1
so_can_so_sanh = 99999999999
is_running = True

print("⚠️ Mở sẵn Word hoặc Excel rồi chạy chương trình.")
print("⌛ Chương trình sẽ bắt đầu sau 3 giây. Nhấn ESC bất cứ lúc nào để dừng.")
time.sleep(1)

while is_running:
    if keyboard.is_pressed('esc'):
        print("\n⏹ Chương trình đã dừng nhập.")
        is_running = False
        break

    # Xóa dòng trước đó
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')

    # Gõ dòng mới (không nhấn enter nữa)
    pyautogui.write(f"{so_bat_dau}", interval=0.1)

    # Kiểm tra nếu đúng thì dừng
    if so_bat_dau == so_can_so_sanh:
        break

    so_bat_dau += 1
    time.sleep(0.5)

print("✅ Chương trình kết thúc!")



