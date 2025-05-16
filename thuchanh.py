import sys
import time
import random
import os

def hieu_ung_xuat(chuoi, toc_do=0.05):
    """Hiển thị từng chữ một với hiệu ứng."""
    for char in chuoi:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(toc_do)
    print()  # Xuống dòng sau khi in xong

def hieu_ung_xoa(toc_do=0.02):
    """Tạo hiệu ứng làm mờ màn hình."""
    print("\n" * 5)
    time.sleep(toc_do)

def lam_moi():
    """Xóa toàn bộ màn hình tùy hệ điều hành."""
    os.system('cls' if os.name == 'nt' else 'clear')

# Danh sách câu hỏi và phản hồi
cau_hoi_ngau_nhien = [
    ("Chọn 1 hoặc 2", "1", "2"),
    ("Chọn 7 hoặc 9", "7", "9"),
    ("Chọn A hoặc B", "A", "B"),
    ("Chọn Trái hoặc Phải", "Trái", "Phải"),
    ("Mèo hay Chó?", "Mèo", "Chó"),
    ("Cơm hay Mì?", "Cơm", "Mì"),
    ("Skibidi hay Rizz?", "Skibidi", "Rizz")
]

phan_hoi_dung = [
    "CHUẨN RỒI NHÓC!",
    "TÔI BIẾT MÀ, MÀY THÍCH!",
    "ĐÚNG CMNR!",
    "MÀY KHÁ ĐẤY!",
    "OK, TÔI CÔNG NHẬN!"
]

phan_hoi_sai = [
    "SAI GÒI NHÓC!",
    "NGÁO À?",
    "VỀ HỌC LẠI ĐI!",
    "THUA RỒI CÒN GÌ!",
    "SAI MỘT LI, ĐI MỘT DẶM!"
]

def choi():
    while True:
        lam_moi()
        hieu_ung_xuat("==== WELCOME TO NGÁO GAME ====")
        cau_hoi, phai_chon1, phai_chon2 = random.choice(cau_hoi_ngau_nhien)

        hieu_ung_xuat(f"\n{cau_hoi}")
        lua_chon = input("Nhập lựa chọn của mày: ").strip()

        if lua_chon.lower() in (phai_chon1.lower(), phai_chon2.lower()):
            hieu_ung_xuat(random.choice(phan_hoi_dung))
        else:
            hieu_ung_xuat(random.choice(phan_hoi_sai))

        tiep = input("\nTiếp tục không? (Enter để chơi tiếp, gõ 'thoat' để nghỉ): ").strip()
        if tiep.lower() == "thoat":
            hieu_ung_xuat("Tạm biệt đồ ngáo!")
            break
        hieu_ung_xoa()

if __name__ == "__main__":
    choi()
