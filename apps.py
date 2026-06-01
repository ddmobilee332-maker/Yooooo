import time
from config import COLOR_RED, COLOR_RESET, COLOR_GREEN, COLOR_WHITE

class AppStore:
    def open(self):
        print("\n--- 🛍️ ยินดีต้อนรับสู่ PlayStore จำลอง ---")
        print("1.ดาวน์โหลด TikTok\n2.ดาวน์โหลด Facebook\n3.กลับหน้าโฮม")
        choice = input("เลือกดาวน์โหลดแอป > ")
        if choice == "1":
            print("[*] กำลังติดตั้ง TikTok...")
            time.sleep(1.5)
            print("[✓] ติดตั้งสำเร็จ!")
            return "TikTok"
        elif choice == "2":
            print("[*] กำลังติดตั้ง Facebook...")
            time.sleep(1.5)
            print("[✓] ติดตั้งสำเร็จ!")
            return "Facebook"
        return None

class YouTube:
    def open(self):
        print(f"\n{COLOR_RED}--- 📺 YouTube จำลอง กำลังสตรีมมิ่ง ---{COLOR_RESET}")
        print("[1] ดูคลิปสอนเขียนสคริปต์ Roblox\n[2] ดูคลิปไฮไลท์ Hackแฮกเกอร์\n[3] ปิด YouTube")
        action = input("เลือกวิดีโอ > ")
        if action in ["1", "2"]:
            print(f"{COLOR_GREEN}[▶] วิดีโอกำลังเล่นอยู่... (กด Enter เพื่อหยุดเล่น){COLOR_RESET}")
            input()
        print("ปิดแอป YouTube เรียบร้อย")

class GameManager:
    def open(self):
        print("\n--- 🎮 คลังเกมจำลอง ---")
        print("[1] รันเกม Roblox OS\n[2] ปิดเมนูเกม")
        action = input("เลือกคำสั่ง > ")
        if action == "1":
            print("[*] กำลังโหลดแมพและรันระบบเซิร์ฟเวอร์เสมือน...")
            time.sleep(2)
            print("[✓] เข้าเกมสำเร็จ! คุณสามารถเล่นได้ปกติในหน้านี้ (กด Enter เพื่อออกจากเกม)")
            input()
          
