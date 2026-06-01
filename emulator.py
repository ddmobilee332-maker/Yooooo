import os
import time
from config import COLOR_RED, COLOR_DARK, COLOR_RESET, COLOR_GREEN, COLOR_WHITE
from apps import AppStore, YouTube, GameManager
from terminal import CyberTerminal

class VirtualPhone:
    def __init__(self):
        self.is_running = False
        self.installed_apps = ["YouTube", "PlayStore", "Games", "Terminal >_"]
        self.store = AppStore()
        self.youtube = YouTube()
        self.games = GameManager()
        self.terminal = CyberTerminal()

    def boot_system(self):
        self.is_running = True
        self.phone_interface()

    def phone_interface(self):
        while self.is_running:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{COLOR_RED}====================================={COLOR_RESET}")
            print(f"{COLOR_WHITE}      📱 VIRTUAL PHONE OS (จำลอง)     {COLOR_RESET}")
            print(f"{COLOR_RED}====================================={COLOR_RESET}")
            print(f"{COLOR_DARK} สถานะ: กำลังใช้งานจริง | แบตเตอรี่: 100%{COLOR_RESET}\n")
            
            print(f"{COLOR_WHITE}[ แอปพลิเคชันทั้งหมดบนเครื่อง ]{COLOR_RESET}")
            for index, app in enumerate(self.installed_apps, 1):
                print(f" {index}. {app}")
            
            print(f"\n{COLOR_RED}[0] กดออกจากแอป (กลับหน้าหลัก db.exe){COLOR_RESET}")
            
            choice = input(f"\n{COLOR_GREEN}เลือกแอปที่ต้องการเปิด > {COLOR_RESET}").strip()
            
            if choice == "1":
                self.youtube.open()
            elif choice == "2":
                new_app = self.store.open()
                if new_app and new_app not in self.installed_apps:
                    self.installed_apps.append(new_app)
            elif choice == "3":
                self.games.open()
            elif choice == "4":
                self.terminal.open_shell()
            elif choice == "0":
                print(f"{COLOR_DARK}กำลังออกจากระบบจำลองโทรศัพท์...{COLOR_RESET}")
                time.sleep(1)
                self.is_running = False
            else:
                print(f"{COLOR_RED}[!] ไม่พบแอปนี้บนหน้าจอ{COLOR_RESET}")
                time.sleep(1)
              
