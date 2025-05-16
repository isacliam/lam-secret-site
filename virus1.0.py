from pynput import keyboard
import ctypes
import sys

# Hỏi người dùng bằng hộp thoại Yes/No
response = ctypes.windll.user32.MessageBoxW(0, "Bạn có muốn bắt đầu ghi phím không?Nếu bắt đầu các phím bạn gõ sẽ được ghi lại.", "Xác nhận", 4)

# Nếu người dùng chọn No (2), thì thoát luôn
if response == 7:
    sys.exit("Đã hủy chương trình.")

def on_press(key):
    try:
        if key == keyboard.Key.enter:
            key = "\n"
        elif key == keyboard.Key.esc:
            raise SystemExit(0)
        with open("result.txt", "a", encoding="utf-8") as file:
            file.write(str(key.char))
        print(key)
    except AttributeError:
        with open("result.txt", "a", encoding="utf-8") as file:
            file.write(f"[{key}]")
        print(key)

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# Sau khi kết thúc ghi
ctypes.windll.user32.MessageBoxW(0, "Chương trình đã dừng", "Thông báo", 0)

