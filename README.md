# 🤖 Offline AI Chatbot with DialoGPT

This is a **locally running chatbot** using **DialoGPT-small** and PyTorch, with a Tkinter-based GUI.

## 📂 Project Structure

chatbot_project/
├── models/                      # Stores DialoGPT-small model
│   ├── config.json
│   ├── model.safetensors
│   ├── tokenizer.json
│   ├── vocab.json
│   └── ...
├── utils/                       # Utility functions (config, logging, text processing)
│   ├── config.py
│   ├── logger.py
│   ├── text_utils.py
│   └── __init__.py
├── logs/                        # Logs for debugging and conversation tracking
│   ├── chatbot.log
│   ├── errors.log
│   └── logger.py
├── gui/                         # GUI chatbot application
│   ├── chatbot_gui.py
│   └── __init__.py
├── models/                      # Handles model loading and response generation
│   ├── load_model.py
│   ├── generate_response.py
│   └── __init__.py
├── settings.yaml                 # 🔧 Project settings (model, paths, GUI options)
├── requirements.txt              # 📦 Python dependencies
├── run_chatbot.py                # ▶️ Main entry point for chatbot GUI
├── README.md                     # 📖 Project Documentation
└── .gitignore                     # 🚫 Ignore unnecessary files


