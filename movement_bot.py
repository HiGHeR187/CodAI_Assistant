import threading
import keyboard
import time

running = False
thread = None

def move_loop():
    while running:
        keyboard.press('w')
        time.sleep(0.1)
        keyboard.release('w')
        time.sleep(0.2)

def start_movement():
    global running, thread
    if not running:
        print("[BOT] Starting movement...")
        running = True
        thread = threading.Thread(target=move_loop, daemon=True)
        thread.start()

def stop_movement():
    global running
    if running:
        print("[BOT] Stopping movement...")
        running = False
