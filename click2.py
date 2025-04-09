import pyautogui
import keyboard
import threading
import time

class AutoClicker:
    def __init__(self):
        self.clicking = False
        self.delay = 0.0  # 2 segundos entre cliques (ajuste conforme necessário)
        self.hotkey = 'F6'  # Tecla para ativar/desativar
        
    def start_clicking(self):
        while True:
            if self.clicking:
                pyautogui.click()
                time.sleep(self.delay)  # Delay em segundos
            else:
                time.sleep(0.1)  # Evita uso excessivo da CPU
    
    def toggle_clicking(self):
        self.clicking = not self.clicking
        status = "ATIVADO" if self.clicking else "DESATIVADO"
        print(f"Autoclicker {status} (Pressione {self.hotkey} para alternar)")
    
    def run(self):
        print(f"Autoclicker - Pressione {self.hotkey} para começar/parar (ESC para sair)")
        keyboard.add_hotkey(self.hotkey, self.toggle_clicking)
        
        click_thread = threading.Thread(target=self.start_clicking)
        click_thread.daemon = True
        click_thread.start()
        
        keyboard.wait('esc')  # Pressione ESC para encerrar o programa

if __name__ == "__main__":
    autoclicker = AutoClicker()
    autoclicker.run()