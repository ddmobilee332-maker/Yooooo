import os
import time
from config import COLOR_RED, COLOR_DARK, COLOR_RESET, COLOR_WHITE, SYSTEM_VERSION
from emulator import VirtualPhone

def load_logo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(COLOR_RED)
    try:
        with open("logo.txt", "r", encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        print("[!] ไม่พบไฟล์ logo.txt")
    print(COLOR_DARK + f" --- Ruenyai HUB Cyber System {SYSTEM_VERSION} ---" + COLOR_RESET)

def main_menu():
    phone = VirtualPhone()
    while True:
        load_logo()
        print(f"\n{COLOR_WHITE}[ เมนูควบคุมคำสั่งหลัก ]{COLOR_RESET}")
        print(f"{COLOR_RED}[oopp]{COLOR_RESET} - เปิดใช้งานระบบจำลองโทรศัพท์อีกเครื่อง")
        print(f"{COLOR_RED}[exit]{COLOR_RESET} - ปิดโปรแกรม")
        
        cmd = input(f"\n{COLOR_RED}Ruenyai_HUB > {COLOR_RESET}").strip()
        
        if cmd.lower() == "oopp":
            print(f"\n{COLOR_GREEN}[*] กำลังสร้างสภาพแวดล้อมจำลอง... กรุณารอระบบเด้งเข้าหน้าต่างใหม่{COLOR_RESET}")
            time.sleep(2)
            phone.boot_system()
        elif cmd.lower() == "exit":
            print(f"{COLOR_DARK}กำลังปิดระบบ... สวัสดีค่ะ{COLOR_RESET}")
            break
        else:
            print(f"{COLOR_RED}[!] ไม่พบคำสั่งนี้ กรุณาลองใหม่{COLOR_RESET}")
            time.sleep(1)

if __name__ == "__main__":
    main_menu()
  
