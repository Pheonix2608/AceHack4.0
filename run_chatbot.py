import yaml
from gui.chatbot_gui import ChatBotGUI
import tkinter as tk

# Load settings from YAML file
# Ensure the settings.yaml file is in the same directory as this script or provide the correct path
with open(r"F:\Projects\NLP\chatbot_project\settings.yaml", "r") as file:
    settings = yaml.safe_load(file)

# Start GUI
if __name__ == "__main__":
    root = tk.Tk()
    root.title(settings["gui"]["title"])
    root.geometry(f"{settings['gui']['width']}x{settings['gui']['height']}")
    
    app = ChatBotGUI(root)
    root.mainloop()
