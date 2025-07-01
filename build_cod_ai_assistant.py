
Create a file named build_cod_ai_assistant.py and paste this code:

python
Copy
Edit
import os
import subprocess
import shutil
import whisper

APP_NAME = "CodAIAssistant"
ENTRY_SCRIPT = "gui.py"
DIST_DIR = "dist"

def install_requirements():
    print("[1/5] Installing dependencies...")
    subprocess.run(["pip", "install", "--upgrade", "pip"])
    subprocess.run(["pip", "install", "-r", "requirements.txt"])

def download_whisper_model():
    print("[2/5] Downloading Whisper model (base)...")
    whisper.load_model("base")

def build_exe():
    print("[3/5] Compiling EXE with PyInstaller...")
    subprocess.run([
        "pyinstaller",
        "--onefile",
        "--noconsole",
        "--name", APP_NAME,
        ENTRY_SCRIPT
    ])

def collect_resources():
    print("[4/5] Assembling ZIP folder...")
    if os.path.exists("CodAI_Assistant"):
        shutil.rmtree("CodAI_Assistant")
    os.makedirs("CodAI_Assistant/resources", exist_ok=True)

    shutil.copy(f"{DIST_DIR}/{APP_NAME}.exe", "CodAI_Assistant/")
    shutil.copy("README.md", "CodAI_Assistant/")
    shutil.copy("requirements.txt", "CodAI_Assistant/")
    shutil.copytree("resources", "CodAI_Assistant/resources", dirs_exist_ok=True)

def zip_package():
    print("[5/5] Creating CodAI_Assistant.zip...")
    shutil.make_archive("CodAI_Assistant", "zip", "CodAI_Assistant")
    print("✅ Build complete! Find CodAI_Assistant.zip in this folder.")

if __name__ == "__main__":
    install_requirements()
    download_whisper_model()
    build_exe()
    collect_resources()
    zip_package()
