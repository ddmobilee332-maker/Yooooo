import time
from config import COLOR_RED, COLOR_RESET, COLOR_GREEN, COLOR_DARK

class CyberTerminal:
    def open_shell(self):
        print(f"\n{COLOR_DARK}[ เปิดการเชื่อมต่อคอนโซลภายใน >_ ]{COLOR_RESET}")
        while True:
            cmd = input(f"{COLOR_GREEN}root@virtual_device:~# {COLOR_RESET}").strip()
            if cmd.lower() == "exit":
                print("ปิดหน้าจอคอนโซล...")
                break
            elif cmd.lower() == "help":
                print("คำสั่งที่ใช้งานได้: help, ping, hack-start, exit")
            elif cmd.lower() == "ping":
                print("64 bytes from 127.0.0.1: icmp_seq=1 ttl=64 time=0.045 ms")
            elif cmd.lower() == "hack-start":
                print(f"{COLOR_RED}[!] กำลังจำลองการ Bypass พอร์ตระบบรักษาความปลอดภัย...{COLOR_RESET}")
                time.sleep(1)
                print(f"{COLOR_GREEN}[✓] เจาะระบบเสร็จสิ้น ดึงข้อมูลสำเร็จ!{COLOR_RESET}")
            else:
                print(f"bash: {cmd}: ไม่พบคำสั่งนี้ (พิมพ์ help เพื่อดูคำสั่ง)")
              
