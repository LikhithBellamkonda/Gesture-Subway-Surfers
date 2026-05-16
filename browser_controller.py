from pynput.keyboard import Controller, Key
import threading

class BrowserController:
    def __init__(self):
        self.keyboard = Controller()
        self.current_state_running = True # Assume running

    def _press_key(self, key):
        self.keyboard.press(key)
        self.keyboard.release(key)

    def move_left(self):
        threading.Thread(target=self._press_key, args=(Key.left,)).start()

    def move_right(self):
        threading.Thread(target=self._press_key, args=(Key.right,)).start()

    def jump(self):
        threading.Thread(target=self._press_key, args=(Key.up,)).start()

    def slide(self):
        threading.Thread(target=self._press_key, args=(Key.down,)).start()

    def toggle_pause(self, is_running):
        if is_running and not self.current_state_running:
            # Resume
            threading.Thread(target=self._press_key, args=(Key.space,)).start()
            self.current_state_running = True
        elif not is_running and self.current_state_running:
            # Pause
            threading.Thread(target=self._press_key, args=(Key.space,)).start() # Or ESC
            self.current_state_running = False
