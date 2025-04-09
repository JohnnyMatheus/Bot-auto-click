import pyautogui
import keyboard
import threading
import time

class RapidClicker:
    def __init__(self):
        self.clicking = False
        self.max_clicks = 1000
        self.current_clicks = 0
        self.delay = 0.01  # 10ms entre cliques (muito rápido)
        self.hotkey = 'F6'  # Tecla para iniciar/parar
        
    def start_clicking(self):
        self.current_clicks = 0
        while self.current_clicks < self.max_clicks and self.clicking:
            pyautogui.click()
            self.current_clicks += 1
            time.sleep(self.delay)
            # Atualiza o contador no console
            print(f"\rCliques: {self.current_clicks}/{self.max_clicks}", end="")
        self.clicking = False
        print("\n1000 cliques concluídos!" if self.current_clicks >= self.max_clicks 
              else "\nInterrompido pelo usuário")
    
    def toggle_clicking(self):
        if not self.clicking:
            self.clicking = True
            click_thread = threading.Thread(target=self.start_clicking)
            click_thread.daemon = True
            click_thread.start()
            print(f"Iniciando 1000 cliques rápidos (Pressione {self.hotkey} para parar)")
        else:
            self.clicking = False
            print("Parando...")
    
    def run(self):
        print(f"Rapid Clicker 1000 - Pressione {self.hotkey} para iniciar")
        print(f"Pressione ESC para sair do programa")
        keyboard.add_hotkey(self.hotkey, self.toggle_clicking)
        keyboard.wait('esc')  # Pressione ESC para sair

if __name__ == "__main__":
    clicker = RapidClicker()
    clicker.run()