import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import threading
import subprocess
import time
import voice_interface
import movement_bot

class CodAIAssistantApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cod AI Assistant")
        self.root.geometry("800x600")

        self.tab_control = ttk.Notebook(root)

        self.voice_tab = ttk.Frame(self.tab_control)
        self.bot_tab = ttk.Frame(self.tab_control)
        self.code_tab = ttk.Frame(self.tab_control)
        self.settings_tab = ttk.Frame(self.tab_control)

        self.tab_control.add(self.voice_tab, text="🎙️ Voice Assistant")
        self.tab_control.add(self.bot_tab, text="🎮 Game Bot")
        self.tab_control.add(self.code_tab, text="💻 Run Code")
        self.tab_control.add(self.settings_tab, text="⚙️ Settings")

        self.tab_control.pack(expand=1, fill="both")

        self.create_voice_tab()
        self.create_bot_tab()
        self.create_code_tab()
        self.create_settings_tab()

    def create_voice_tab(self):
        label = tk.Label(self.voice_tab, text="Press start and speak your command...", font=("Segoe UI", 12))
        label.pack(pady=10)

        self.transcription_box = scrolledtext.ScrolledText(self.voice_tab, wrap=tk.WORD, height=10)
        self.transcription_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        start_btn = ttk.Button(self.voice_tab, text="Start Listening", command=self.start_voice_thread)
        start_btn.pack(pady=5)

    def start_voice_thread(self):
        threading.Thread(target=self.run_voice_recognition, daemon=True).start()

    def run_voice_recognition(self):
        self.transcription_box.insert(tk.END, "[Listening...]\n")
        result = voice_interface.listen_and_transcribe()
        self.transcription_box.insert(tk.END, f"> {result}\n")

        if "start movement" in result.lower():
            movement_bot.start_movement()
        elif "stop movement" in result.lower():
            movement_bot.stop_movement()

    def create_bot_tab(self):
        ttk.Label(self.bot_tab, text="Manual Game Bot Control", font=("Segoe UI", 12)).pack(pady=10)

        ttk.Button(self.bot_tab, text="Start Movement Bot", command=movement_bot.start_movement).pack(pady=5)
        ttk.Button(self.bot_tab, text="Stop Movement Bot", command=movement_bot.stop_movement).pack(pady=5)

    def create_code_tab(self):
        ttk.Label(self.code_tab, text="Run Python Code", font=("Segoe UI", 12)).pack(pady=10)

        self.code_input = scrolledtext.ScrolledText(self.code_tab, wrap=tk.WORD, height=10)
        self.code_input.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        ttk.Button(self.code_tab, text="Run Code", command=self.execute_code).pack(pady=5)

        self.code_output = scrolledtext.ScrolledText(self.code_tab, wrap=tk.WORD, height=10, state='disabled')
        self.code_output.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    def execute_code(self):
        code = self.code_input.get("1.0", tk.END)
        try:
            output = subprocess.check_output(["python", "-c", code], stderr=subprocess.STDOUT, text=True)
        except subprocess.CalledProcessError as e:
            output = e.output
        self.code_output.configure(state='normal')
        self.code_output.insert(tk.END, output + "\n")
        self.code_output.configure(state='disabled')

    def create_settings_tab(self):
        ttk.Label(self.settings_tab, text="Settings (future expansion)", font=("Segoe UI", 12)).pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = CodAIAssistantApp(root)
    root.mainloop()
